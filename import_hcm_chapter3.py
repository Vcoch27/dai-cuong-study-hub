"""Import only chapter 3 from the supplied Markdown; retain every text page."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent / 'content' / 'hcm'


def run():
    source = (ROOT / 'source-chapters-3-4.md').read_text(encoding='utf-8-sig')
    blocks = re.split(r'<!-- Chương (\d+), slide (\d+)/(\d+) -->', source)
    sections = []
    for i in range(1, len(blocks), 4):
        chapter, page, total = map(int, blocks[i:i+3])
        if chapter != 3:
            continue
        text = re.sub(r'<details>.*?</details>', '', blocks[i+3], flags=re.S)
        text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
        text = re.sub(r'^\*\*Slide \d+/\d+ – Chương 3\*\*\s*', '', text.strip())
        text = re.sub(r'^---\s*$', '', text, flags=re.M)
        # Markdown becomes plain text in the existing reader and evidence pane.
        text = re.sub(r'^#{1,6}\s*|^>\s?', '', text, flags=re.M)
        text = text.replace('**', '').replace('*', '')
        text = re.sub(r'\n{3,}', '\n\n', text).strip()
        title = text.splitlines()[0]
        if len(title) > 125:
            title = f'Nội dung trang {page}'
        sections.append({'id': f'hcm-c3-p{page:02}', 'chapter': 3,
                         'page': page, 'title': title, 'text': text})
    assert [s['page'] for s in sections] == list(range(1, 70))
    data = json.loads((ROOT / 'content.json').read_text(encoding='utf-8-sig'))
    data['chapters'] = [c for c in data['chapters'] if c['id'] != 3] + [{
        'id': 3, 'title': 'Độc lập dân tộc và chủ nghĩa xã hội',
        'topics': ['Độc lập dân tộc và cách mạng giải phóng dân tộc',
                   'Chủ nghĩa xã hội và xây dựng chủ nghĩa xã hội ở Việt Nam',
                   'Thời kỳ quá độ lên chủ nghĩa xã hội',
                   'Quan hệ giữa độc lập dân tộc và chủ nghĩa xã hội',
                   'Vận dụng trong sự nghiệp cách mạng Việt Nam']}]
    data['sections'] = [s for s in data['sections'] if s['chapter'] != 3] + sections
    assert len(data['sections']) == 131
    (ROOT / 'content.json').write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    print('Imported chapter 3: all 69 text pages. Chapter 4 excluded.')


if __name__ == '__main__':
    run()
