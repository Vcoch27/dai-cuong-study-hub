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
    authored = '\n'.join((DIRECTORY / name).read_text(encoding='utf-8') for name in ('authored_questions.txt', 'authored_chapter3.txt'))
    rows = [line for line in authored.splitlines()
            if line.strip() and not line.startswith('#')]
    slots = [i % 4 for i in range(len(rows))]
    random.Random(20261022).shuffle(slots)
    chapter3_slots = [index % 4 for index in range(120)]
    random.Random(20261023).shuffle(chapter3_slots)
    counters = Counter()
    questions = []
    for row, slot in zip(rows, slots):
        parts = [part.strip() for part in row.split('|')]
        assert len(parts) == 10 and all(parts), row
        chapter, page, kind, difficulty, stem, key, *rest = parts
        chapter, page = int(chapter), int(page)
        counters[chapter] += 1
        qid = f'hcm-c{chapter}-q{counters[chapter]:03}'
        if chapter == 3:
            slot = chapter3_slots[counters[chapter] - 1]
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
    assert len(questions) == 240 and counters == {1: 30, 2: 90, 3: 120}
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
    # Existing forms and attempts stay stable; add chapter 3 forms once.
    chapter3 = [q for q in questions if q['id'].startswith('hcm-c3-')]
    chapter3_buckets = [[] for _ in range(4)]
    # Round robin within topics keeps every form spread across the whole chapter.
    for index, question in enumerate(chapter3):
        chapter3_buckets[index % 4].append(question['id'])
    for index in range(4):
        form_id = f'hcm-chapter3-{index+1}'
        if any(form['id'] == form_id for form in forms):
            continue
        ids = chapter3_buckets[index]
        random.Random(20261023 + index).shuffle(ids)
        forms.append({'id': form_id, 'title': f'Chương 3 · Đề {index+1}',
                      'focus': 'Độc lập dân tộc, giải phóng dân tộc, xây dựng CNXH và thời kỳ quá độ.',
                      'durationSeconds': 900, 'questionIds': ids})
    (DIRECTORY / 'questions.json').write_text(
        json.dumps({'questions': questions, 'examForms': forms}, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Compiled {len(questions)} authored questions and {len(forms)} fixed exam forms')


if __name__ == '__main__':
    compile_bank()
