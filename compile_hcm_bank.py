"""Compile explicitly authored items; randomize answer slots once with a fixed seed."""
import json
import random
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parent
DIRECTORY = ROOT / 'content' / 'hcm'


def compile_bank():
    previous_path = DIRECTORY / 'questions.json'
    previous = json.loads(previous_path.read_text(encoding='utf-8-sig')) if previous_path.exists() else {}
    previous_items = {item['id']: item for item in previous.get('questions', [])}
    rows = [line for line in (DIRECTORY / 'authored_questions.txt').read_text(encoding='utf-8').splitlines()
            if line.strip() and not line.startswith('#')]
    slots = [i % 4 for i in range(len(rows))]
    random.Random(20261022).shuffle(slots)
    counters = Counter()
    questions = []
    for row, slot in zip(rows, slots):
        parts = [part.strip() for part in row.split('|')]
        assert len(parts) == 10 and all(parts), row
        chapter, page, kind, difficulty, stem, key, *rest = parts
        chapter, page = int(chapter), int(page)
        counters[chapter] += 1
        qid = f'hcm-c{chapter}-q{counters[chapter]:03}'
        choices = rest[:3]
        random.Random(qid).shuffle(choices)
        choices.insert(slot, key)
        # Recompiling/appending must not reshuffle already published choices.
        old = previous_items.get(qid)
        if old and set(old['choices']) == set(choices):
            choices = old['choices']
            slot = choices.index(key)
        questions.append({
            'id': qid, 'sectionId': f'hcm-c{chapter}-p{page:02}',
            'question': stem, 'choices': choices, 'answer': slot,
            'explanation': rest[3], 'type': kind, 'difficulty': difficulty,
        })
    assert len(questions) == 120 and counters == {1: 30, 2: 90}
    buckets = [[] for _ in range(4)]
    for chapter in (1, 2):
        for index, question in enumerate(q for q in questions if q['id'].startswith(f'hcm-c{chapter}-')):
            buckets[(index + (2 if chapter == 2 else 0)) % 4].append(question['id'])
    forms = []
    for index, ids in enumerate(buckets, 1):
        assert len(ids) == 30
        random.Random(20261022 + index).shuffle(ids)
        forms.append({
            'id': f'hcm-midterm-{index}', 'title': f'Đề {index} · Tổng hợp chương 1–2',
            'focus': 'Trộn khái niệm, phương pháp, cơ sở hình thành, tiến trình lịch sử và giá trị tư tưởng.',
            'durationSeconds': 900, 'questionIds': ids,
        })
    if previous.get('examForms'):
        forms = previous['examForms']
    (DIRECTORY / 'questions.json').write_text(
        json.dumps({'questions': questions, 'examForms': forms}, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Compiled {len(questions)} authored questions and {len(forms)} fixed exam forms')


if __name__ == '__main__':
    compile_bank()
