"""Import the user's formatted text verbatim with stable source occurrence IDs."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
DIRECTORY = ROOT / 'content/hcm-bank'


def parse(text):
    document = 0
    part = 'mcq'
    group = None
    titles = {}
    records = []
    current = None
    for line in text.splitlines():
        document_match = re.match(r'TÀI LIỆU (\d+):\s*(.+)', line)
        if document_match:
            document = int(document_match[1])
            titles[document] = document_match[2]
            part = 'mcq'
            group = None
        group_match = re.match(r'NHÓM (\d+)', line)
        if group_match:
            group = int(group_match[1])
        if line.startswith('PHẦN 1:'):
            part = 'short'
        elif line.startswith('PHẦN 2:'):
            part = 'mcq'
        question_match = re.match(r'Câu\s+(\d+)\s*(\[TỰ LUẬN\])?\.\s*(.*)', line)
        if question_match:
            if current:
                records.append(current)
            number = int(question_match[1])
            subgroup = f'g{group or 1}' if document == 2 else part
            current = {'id': f't{document}-{subgroup}-{number:02}', 'setId': f'tap-{document}', 'subgroup': subgroup,
                       'document': document, 'part': part, 'number': number,
                       'kind': 'essay' if question_match[2] else 'short' if part == 'short' else 'mcq',
                       'question': question_match[3], 'choices': [], 'providedAnswer': None, 'page': None, 'notes': []}
            continue
        if not current:
            continue
        option = re.match(r'\s+([ABCD])\.\s*(.*)', line)
        answer = re.match(r'\s*(?:Đáp án trong tài liệu|Trả lời theo nguồn):\s*(.*)', line)
        page = re.search(r'\(Nguồn: tài liệu (\d+), trang (\d+)\)', line)
        if option:
            assert ord(option[1])-65 == len(current['choices']), current['id']
            current['choices'].append(option[2])
        elif answer:
            current['providedAnswer'] = answer[1]
            current['kind'] = 'short'
        elif page:
            assert int(page[1]) == current['document']
            current['page'] = int(page[2])
        elif '[CẦN ĐỐI CHIẾU]' in line:
            current['notes'].append(line.strip())
    if current:
        records.append(current)
    assert len(records) == len({record['id'] for record in records}) == 261
    return {'sets': [{'id': f'tap-{key}', 'title': f'Tập {key}', 'description': title} for key,title in titles.items()],
            'records': records}


if __name__ == '__main__':
    result = parse((DIRECTORY / 'source.txt').read_text(encoding='utf-8-sig'))
    (DIRECTORY / 'imported.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f"Imported {len(result['records'])} source occurrences in {len(result['sets'])} sets")
