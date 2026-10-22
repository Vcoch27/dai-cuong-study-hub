"""Build HCM study data from supplied text and an authored question bank; no PDF parsing."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
INPUT = ROOT / 'content' / 'hcm'


def build():
    content = json.loads((INPUT / 'content.json').read_text(encoding='utf-8-sig'))
    bank = json.loads((INPUT / 'questions.json').read_text(encoding='utf-8-sig'))
    chapters = {item['id']: item for item in content['chapters']}
    assert len(chapters) == len(content['chapters']) and chapters, 'Chapter IDs must be unique'
    sections = {item['id']: item for item in content['sections']}
    assert len(sections) == len(content['sections']), 'Section IDs must be unique'
    for item in sections.values():
        assert item['chapter'] in chapters and item['title'].strip() and item['text'].strip()
        assert item.get('page') is None or isinstance(item['page'], int) and item['page'] > 0
    questions = []
    for item in bank['questions']:
        assert item['id'].startswith('hcm-') and item['question'].strip()
        assert not re.search(r'ghi chú|\bslide\b|tài liệu|trong bài', item['question'], re.I), item['id']
        assert len(item['choices']) == len(set(item['choices'])) == 4
        assert all(isinstance(choice, str) and choice.strip() for choice in item['choices'])
        assert type(item['answer']) is int and 0 <= item['answer'] < 4 and item['explanation'].strip()
        section = sections[item['sectionId']]
        label = f"Chương {section['chapter']} · {section['title']}"
        if section.get('page'):
            label += f" · Trang {section['page']}"
        questions.append({key: item[key] for key in ('id', 'question', 'choices', 'answer', 'explanation', 'type', 'difficulty') if key in item} | {
            'chapter': section['chapter'],
            'source': {'kind': 'text', 'sectionId': section['id'], 'label': label, 'evidence': section['text']},
        })
    ids = {item['id'] for item in questions}
    assert len(ids) == len(questions), 'Question IDs must be unique and stable'
    assert len({item['question'] for item in questions}) == len(questions), 'Duplicate question stems'
    forms = bank.get('examForms', [])
    assert len({form['id'] for form in forms}) == len(forms)
    for form in forms:
        assert form['id'].startswith('hcm-') and form['title'].strip() and form['focus'].strip()
        assert len(form['questionIds']) == len(set(form['questionIds'])) == 30
        assert set(form['questionIds']) <= ids and form['durationSeconds'] == 900
    output = {
        'course': content['course'], 'chapters': content['chapters'],
        # Keep this stable when adding new questions; existing progress must survive.
        'questionRevision': 'v1', 'questions': questions, 'examForms': forms,
        'studySections': list(sections.values()), 'docLines': [], 'slidePages': [],
    }
    target = ROOT / 'dist' / 'hcm-data.json'
    from hcm_slide_sources import attach_course
    attach_course(output)
    target.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'HCM: {len(chapters)} chapters, {len(sections)} text sections, {len(questions)} questions, {len(forms)} exams')
    return output


if __name__ == '__main__':
    build()
