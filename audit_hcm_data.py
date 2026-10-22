"""Check source references, coverage and superficial answer cues for the HCM bank."""
import json
from collections import Counter
from pathlib import Path
from audit_questions import metrics

ROOT = Path(__file__).parent


def audit():
    data = json.loads((ROOT / 'dist/hcm-data.json').read_text(encoding='utf-8'))
    source = json.loads((ROOT / 'content/hcm/content.json').read_text(encoding='utf-8'))
    sections = {section['id']: section for section in source['sections']}
    assert len(sections) == 131 and data['studySections'] == source['sections']
    assert Counter(section['chapter'] for section in sections.values()) == {1: 8, 2: 54, 3: 69}
    questions = data['questions']
    assert len(questions) == len({q['id'] for q in questions}) == 240
    assert len({q['question'] for q in questions}) == 240
    assert Counter(q['chapter'] for q in questions) == {1: 30, 2: 90, 3: 120}
    assert Counter(q['answer'] for q in questions) == {0: 60, 1: 60, 2: 60, 3: 60}
    for question in questions:
        section = sections[question['source']['sectionId']]
        assert question['chapter'] == section['chapter']
        assert question['source']['kind'] == 'text'
        assert question['source']['evidence'] == section['text']
        assert question['explanation'].strip()
        assert len(question['choices']) == len(set(question['choices'])) == 4
        assert question['difficulty'] in {'cơ bản', 'phân biệt', 'vận dụng'}
    used = []
    by_id = {question['id']: question for question in questions}
    assert len(data['examForms']) == 8
    for form in data['examForms']:
        ids = form['questionIds']
        assert len(ids) == len(set(ids)) == 30 and form['durationSeconds'] == 900
        assert set(ids) <= set(by_id)
        counts = Counter(by_id[qid]['chapter'] for qid in ids)
        if form['id'].startswith('hcm-chapter3-'):
            assert counts == {3: 30}
            pages = [int(by_id[qid]['source']['sectionId'].split('-p')[1]) for qid in ids]
            assert min(pages) <= 8 and max(pages) >= 64
        else:
            assert counts[1] in (7, 8) and counts[2] in (22, 23)
        used.extend(ids)
    assert len(used) == len(set(used)) == len(questions)
    result = metrics(questions)
    assert not result['length_review_ids'] and not result['distractor_cue_ids'], result
    assert 20 <= result['pick_longest_accuracy_percent'] <= 30
    assert 20 <= result['pick_shortest_accuracy_percent'] <= 30
    chapter3 = [q for q in questions if q['chapter'] == 3]
    chapter3_metrics = metrics(chapter3)
    assert 20 <= chapter3_metrics['pick_longest_accuracy_percent'] <= 30
    assert 20 <= chapter3_metrics['pick_shortest_accuracy_percent'] <= 30
    assert len({q['source']['sectionId'] for q in chapter3}) == 53
    result['chapter3'] = chapter3_metrics
    result['source_pages_in_reader'] = len(sections)
    result['source_pages_used_in_questions'] = len({q['source']['sectionId'] for q in questions})
    result['chapters'] = dict(Counter(q['chapter'] for q in questions))
    result['difficulty'] = dict(Counter(q['difficulty'] for q in questions))
    result['types'] = dict(Counter(q['type'] for q in questions))
    result['exam_forms'] = len(data['examForms'])
    return result


if __name__ == '__main__':
    print(json.dumps(audit(), ensure_ascii=True, indent=2))
