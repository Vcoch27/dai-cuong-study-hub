"""Explicit, reviewed slide links shared by both HCM study tracks."""
import json
from pathlib import Path

ROOT=Path(__file__).parent


def manifest():
    pages=json.loads((ROOT/'content/hcm/slide-manifest.json').read_text(encoding='utf-8'))
    assert len(pages)==175
    return pages


def reviews():
    result={}
    for line in (ROOT/'content/hcm-bank/slide-review.txt').read_text(encoding='utf-8').splitlines():
        if not line.strip() or line.startswith('#'): continue
        slug,status,refs,reason=line.split('|')
        assert status in ('direct','context','none') and slug not in result
        result['bank-'+slug]={'status':status,'refs':[] if refs=='-' else [tuple(map(int,r.split(':'))) for r in refs.split()], 'reason':reason}
    assert len(result)==139
    return result


def attach(question, review, pages):
    index={(p['chapter'],p['slide']):p for p in pages}
    refs=[]
    for key in review['refs']:
        page=index[tuple(key)]
        assert (ROOT/'dist'/page['image'].lstrip('/')).is_file()
        refs.append({'chapter':page['chapter'],'page':page['slide'],'file':page['file']})
    assert bool(refs)==(review['status']!='none')
    question['source']['slides']=refs
    question['source']['slideMatch']={key:review[key] for key in ('status','reason')}


def attach_course(data):
    pages=[p for p in manifest() if p['chapter']<=3]
    data['slidePages']=pages
    for q in data['questions']:
        section_id=q['source']['sectionId']
        page=int(section_id.split('-p')[1])
        attach(q,{'status':'direct','refs':[(q['chapter'],page)],
                  'reason':'Trang PDF gốc tương ứng chính xác với đoạn văn bản đã dùng biên soạn câu hỏi.'},pages)


def attach_bank(data):
    pages=manifest()
    review=reviews()
    original=[q for q in data['questions'] if not q.get('pastExam')]
    assert {q['id'] for q in original}==set(review)
    for q in data['questions']:
        attach(q, q.pop('_slideReview') if '_slideReview' in q else review[q['id']], pages)
    data['slidePages']=pages
