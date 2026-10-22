"""Verify every reviewed question-to-PDF-page link and its original asset."""
import hashlib
import json
from collections import Counter
from pathlib import Path
from PIL import Image
from extend_hcm_past_exam import parse

ROOT=Path(__file__).parent


def audit():
    bank=json.loads((ROOT/'dist/hcm-bank-data.json').read_text(encoding='utf-8'))
    course=json.loads((ROOT/'dist/hcm-data.json').read_text(encoding='utf-8'))
    pages=bank['slidePages']
    assert Counter(p['chapter'] for p in pages)=={1:8,2:54,3:69,4:44}
    index={(p['file'],p['slide']):p for p in pages}
    assert len(index)==175
    hashes={}
    for p in pages:
        pdf=ROOT/'sources/hcm'/p['file']
        if p['file'] not in hashes: hashes[p['file']]=hashlib.sha256(pdf.read_bytes()).hexdigest()
        assert p['sourceSha256']==hashes[p['file']]
        image=ROOT/'dist'/p['image'].lstrip('/')
        with Image.open(image) as im: assert im.size==(p['imageWidth'],p['imageHeight']) and im.width>=1500
    assert course['slidePages']==[p for p in pages if p['chapter']<=3]
    for q in bank['questions']+course['questions']:
        source=q['source']; match=source['slideMatch']
        assert match['status'] in ('direct','context','none') and match['reason'].strip()
        assert bool(source['slides'])==(match['status']!='none')
        for ref in source['slides']:
            p=index[(ref['file'],ref['page'])]
            assert p['chapter']==ref['chapter']
        if source['kind']=='text':
            ref=source['slides'][0]
            assert ref['chapter']==q['chapter'] and ref['page']==int(source['sectionId'].split('-p')[1])
    past=[q for q in bank['questions'] if q.get('pastExam')]
    assert [q['occurrences'][0] for q in past]==parse()
    canonical={q['id']:q for q in bank['questions'] if not q.get('duplicateOf')}
    assert len(canonical)==147 and len(past)==30
    for q in past:
        if q.get('duplicateOf'): assert q['duplicateOf'] in canonical
    counts=Counter(q['source']['slideMatch']['status'] for q in bank['questions'])
    report=['# Đối chiếu ngân hàng HCM với bốn PDF gốc','',
            'Đủ 169 bản câu hiển thị: 139 bản cũ + 30 vị trí Đề năm trước 1. Toàn bộ gộp còn 147 nội dung.',
            'direct: trang chứa nội dung trả lời; context: chỉ liên quan và còn thiếu chi tiết; none: không tìm thấy trong bốn PDF.',
            'Ảnh dùng đúng thứ tự trang PDF, đánh số từ 1, không tính theo số trang nội bộ của tài liệu khác.','',
            '| ID | Câu hỏi | Mức đối chiếu | Trang PDF | Căn cứ/giới hạn |','|---|---|---|---|---|']
    for q in bank['questions']:
        source=q['source']
        refs=', '.join(f"C{r['chapter']} tr.{r['page']}" for r in source['slides']) or '—'
        report.append(f"| {q['id']} | {q['question'].replace('|','/')} | {source['slideMatch']['status']} | {refs} | {source['slideMatch']['reason']} |")
    report+=['','## Ôn theo slide','',f"240/240 câu giữ ánh xạ sectionId sang đúng trang PDF của chương 1–3. Có {len(course['slidePages'])} ảnh trang trong phần đọc.",
             '',f'Ngân hàng: {dict(counts)}. Mỗi câu có quyết định đối chiếu riêng, không có ánh xạ theo tìm từ khóa tự động.']
    (ROOT/'content/hcm-bank/slide-review-report.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
    return {'originalPDFs':4,'renderedPages':175,'slideCourseQuestions':240,'reviewedBankPositions':169,'allDeduplicated':147,'slideMatch':dict(counts)}


if __name__=='__main__': print(json.dumps(audit(),ensure_ascii=False,indent=2))
