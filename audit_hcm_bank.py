"""Audit explicit deduplication, source coverage, added choices and grading boundaries."""
import json
from collections import Counter
from pathlib import Path
from audit_questions import metrics

ROOT = Path(__file__).parent


def audit():
    data = json.loads((ROOT/'dist/hcm-bank-data.json').read_text(encoding='utf-8'))
    source = json.loads((ROOT/'content/hcm-bank/imported.json').read_text(encoding='utf-8'))
    questions = data['questions']
    assert len(questions) == len({q['id'] for q in questions}) == 169
    canonical = [q for q in questions if not q.get('duplicateOf')]
    past = [q for q in questions if q.get('pastExam')]
    assert len(canonical)==147 and len(past)==30
    assert [q['originalNumber'] for q in past]==list(range(1,31))
    original = {r['id']:r for r in source['records']}
    occurrences = [r for q in canonical for r in q['occurrences']]
    assert len(occurrences) == len({r['id'] for r in occurrences}) == 291
    assert {r['id']:r for r in occurrences if not r.get('setTitle')} == original
    assert len(data['sets']) == 7
    assert len(data['sourceMap']) == 291
    for q in questions:
        assert q['setIds'] == list(dict.fromkeys(r['setId'] for r in q['occurrences']))
        assert set(q['groupIds']) == {f"{r['setId']}-{r['subgroup']}" for r in q['occurrences']}
        assert all(data['sourceMap'][r['id']] == (q.get('duplicateOf') or q['id']) for r in q['occurrences'])
        assert q['explanation'].strip() and q['source']['evidence'].strip()
        if q['kind']=='mcq':
            assert type(q['answer']) is int and 0<=q['answer']<4
            assert len(q['choices']) == len(set(q['choices'])) == 4
        else:
            assert q['answer'] is None and q['kind'] in ('pending','essay')
        if q['generatedDistractors']:
            assert q['keyOrigin']=='provided'
            assert q['choices'][q['answer']] == q['occurrences'][0]['providedAnswer'].rstrip('.')
        for ref in q['source']['references']:
            assert ref.get('url','https://local').startswith('https://')
    assert Counter(q['kind'] for q in canonical) == {'mcq':141,'pending':4,'essay':2}
    assert Counter(q['kind'] for q in past) == {'mcq':29,'pending':1}
    added = [q for q in questions if q['generatedDistractors']]
    assert len(added) == 23
    result = metrics(added)
    # Country names naturally vary in character count; no padding to game the check.
    assert set(result['length_review_ids']) <= {'bank-youth-league-place','bank-lenin-reading-country'}
    assert not result['distractor_cue_ids']
    assert 20<=result['pick_longest_accuracy_percent']<=35
    assert 20<=result['pick_shortest_accuracy_percent']<=35
    for item in data['sets']:
        assert item['rawCount']==sum(r['setId']==item['id'] for r in occurrences)
        expected = len(past) if item.get('preservePositions') else sum(item['id'] in q['setIds'] for q in canonical)
        assert item['uniqueCount']==expected
    return {'bank':data['statistics'],'added_distractor_checks':result,
            'sets':{s['id']:{'original':s['rawCount'],'unique':s['uniqueCount']} for s in data['sets']}}


if __name__=='__main__':
    print(json.dumps(audit(),ensure_ascii=True,indent=2))
