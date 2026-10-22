"""Compile a deduplicated, provenance-preserving bank parallel to the slide course."""
import importlib.util
import json
import random
import re
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parent
DIRECTORY = ROOT / 'content/hcm-bank'

REFERENCES = {
 'biography': ('Tiểu sử Hồ Chí Minh · Bảo tàng Hồ Chí Minh', 'https://hochiminh.vn/book/cuoc-doi-su-nghiep/bien-nien-tieu-su-ho-chi-minh/ho-chi-minh-tieu-su-bao-tang-ho-chi-minh-nxb-chinh-tri-quoc-gia-ha-noi-nam-2008-20'),
 'home': ('Hai lần về thăm quê · Tư liệu Hồ Chí Minh','https://hochiminh.vn/tin-tuc/-anh-hang-nghin-thieu-nien-nhi-dong-ve-tham-que-bac-ho-dip-sinh-nhat-cua-nguoi.html'),
 'will': ('Bắt đầu viết Di chúc năm 1965','https://hochiminh.vn/tin-tuc/60-nam-truoc-bac-ho-bat-dau-viet-di-chuc-12311'),
 'father': ('Di tích Nguyễn Sinh Sắc tại Cao Lãnh · Bảo tàng Hồ Chí Minh','https://baotanghochiminh.vn/di-tich-nguyen-sinh-sac-thi-xa-cao-lanh-tinh-dong-thap.htm'),
 'independence1966': ('Lời kêu gọi ngày 17/7/1966 · Bảo tàng Hồ Chí Minh','https://baotanghochiminh.vn/chu-tich-ho-chi-minh-ra-loi-keu-goi-dong-bao-va-chien-si-ca-nuoc.htm'),
 'partyconcept': ('Nhận thức về tư tưởng Hồ Chí Minh · Học viện Chính trị quốc gia','https://hcma1.hcma.vn/Lists/SanPhamTuHoc/Attachments/126/A15.K71%20SPTH%20TTHCM%20%2828.10.2024%29.pdf'),
 'socialistparty': ('Lời kể về tham gia Đảng Xã hội Pháp · Hồ Chí Minh Toàn tập','https://baotanghochiminh.vn/pic/FileLibrary/HO-CHI-MI_636854814846411358.pdf'),
 'unesco': ('Nghị quyết UNESCO năm 1987 · Tư liệu Hồ Chí Minh','https://hochiminh.vn/ho-chi-minh-va-the-gioi/ban-be-quoc-te-voi-ho-chi-minh/nhung-di-san-vuot-thoi-dai-ven-nguyen-tinh-thoi-su-cua-chu-tich-ho-chi-minh-12363'),
 'unity': ('Tư tưởng về đại đoàn kết','https://hochiminh.vn/tu-tuong-dao-duc-ho-chi-minh/noi-dung-tu-tuong-dao-duc/tu-tuong-ho-chi-minh-ve-dai-doan-ket-25'),
 'resistance': ('Khẩu hiệu Trường kỳ kháng chiến, nhất định thắng lợi','https://hochiminh.vn/tin-tuc/truong-ky-khang-chien-nhat-dinh-thang-loi-giai-thoai-dac-biet-ve-8-can-ve-cua-bac-7055'),
 'cadres': ('Tư tưởng về công tác cán bộ','https://hochiminh.vn/tu-tuong-dao-duc-ho-chi-minh/van-dung-tu-tuong-ho-chi-minh-ve-cong-tac-can-bo-trong-giai-doan-hien-nay.html'),
 'human': ('Động lực con người · Học viện Chính trị quốc gia','https://hcma1.hcma.vn/Lists/SanPhamTuHoc/Attachments/498/A14.K72%20TTHCM%20%2827.3.2026%29.pdf'),
 'school': ('Học để làm việc, làm người, làm cán bộ','https://hochiminh.vn/tu-tuong-dao-duc-ho-chi-minh/nghien-cuu-tu-tuong-dao-duc-ho-chi-minh/hoc-tap-va-lam-theo-phuong-phap-luan-ho-chi-minh-trong-cong-cuoc-doi-moi-phat-trien-dat-nuoc-4077'),
 'selfcriticism': ('Đối với mình · Hồ Chí Minh Toàn tập','https://nhandan.vn/doi-voi-minh-post481301.html'),
 'solidarity': ('Tư tưởng về đoàn kết quốc tế','https://hochiminh.vn/tin-tuc/tu-tuong-ho-chi-minh-ve-doan-ket-quoc-te-349'),
}


def clean(value):
    value = unicodedata.normalize('NFC', value)
    repairs = {'bản chât':'bản chất','tô chức':'tổ chức','Hồ Chỉ Minh':'Hồ Chí Minh',
               'tư sẵn':'tư sản','vân đê':'vấn đề','phát triên':'phát triển','thê giới':'thế giới',
               'giá trị truyền thông':'giá trị truyền thống','đúng nhât':'đúng nhất',
               'bắt khuắt':'bất khuất','bất khuât':'bất khuất','trái tìm':'trái tim','kêu căn':'kiêu căng',
               'Tỏ quốc':'Tổ quốc','lãnh thỏ':'lãnh thổ','đẻ tiến':'để tiến','giai cắp':'giai cấp',
               'ám no':'ấm no','nguyên Giáp':'Nguyên Giáp','Hò Chí Minh':'Hồ Chí Minh',
               'máy thời kỳ':'mấy thời kỳ','máy khuynh':'mấy khuynh','VỚi':'với','nưỚc':'nước','giỚi':'giới'}
    for a,b in repairs.items():
        value = value.replace(a,b)
    return re.sub(r'\s+', ' ', value).strip()


def record_text(record):
    lines = [record['question']] + [f'{chr(65+i)}. {choice}' for i,choice in enumerate(record['choices'])]
    if record['providedAnswer']:
        lines.append('Đáp án có sẵn trong nguồn: ' + record['providedAnswer'])
    return '\n'.join(lines)


def build():
    imported = json.loads((DIRECTORY/'imported.json').read_text(encoding='utf-8'))
    records = {record['id']:record for record in imported['records']}
    spec = importlib.util.spec_from_file_location('hcm_bank_editorial', DIRECTORY/'editorial.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    decisions = module.ITEMS
    assigned = [source for item in decisions for source in item['sources']]
    assert len(assigned) == len(set(assigned)) == len(records) == 261
    assert set(assigned) == set(records), set(records)-set(assigned)
    course = json.loads((ROOT/'content/hcm/content.json').read_text(encoding='utf-8'))
    slide_sections = {(s['chapter'],s['page']):s for s in course['sections']}
    short_slots = [i % 4 for i in range(23)]
    random.Random('hcm-bank-first-publication').shuffle(short_slots)
    questions = []
    source_map = {}
    for item in decisions:
        occurrences = [records[key] for key in item['sources']]
        representative = occurrences[0]
        key = item['key']
        is_short = key == 'provided'
        if is_short:
            correct = representative['providedAnswer'].rstrip('.')
            choices = [clean(value) for value in item['choices']]
            random.Random(item['slug']).shuffle(choices)
            answer = short_slots.pop()
            choices.insert(answer,correct)
        else:
            choices = [clean(value) for value in (item['choices'] or representative['choices'])]
            answer = ord(key)-65 if key not in ('?', 'E') else None
        kind = 'essay' if key=='E' else 'pending' if key=='?' else 'mcq'
        assert kind != 'mcq' or len(choices) == len(set(choices)) == 4, item['slug']
        refs = []
        for ref in item['refs']:
            match = re.fullmatch(r's([12])p(\d+)',ref)
            if match:
                section = slide_sections[(int(match[1]),int(match[2]))]
                refs.append({'title':f"Nội dung lớp · Chương {section['chapter']}, trang {section['page']}", 'text':section['text']})
            elif ref in REFERENCES:
                title,url = REFERENCES[ref]
                refs.append({'title':title,'url':url})
            else:
                raise ValueError(ref)
        question = {
            'id':f"bank-{item['slug']}", 'kind':kind, 'chapter':0,
            'question':clean(item['question'] or representative['question']), 'choices':choices,
            'answer':answer, 'explanation':item['explanation'],
            'keyOrigin':'provided' if is_short else 'editorial' if kind=='mcq' else kind,
            'generatedDistractors':is_short, 'editorialNote':item['note'],
            'setIds':list(dict.fromkeys(record['setId'] for record in occurrences)),
            'groupIds':list(dict.fromkeys(f"{record['setId']}-{record['subgroup']}" for record in occurrences)),
            'occurrences':occurrences,
            'source':{'kind':'bank','label':f"Tập {representative['document']} · Câu {representative['number']:02}",
                      'evidence':record_text(representative),'references':refs},
        }
        for record in occurrences:
            source_map[record['id']] = question['id']
        questions.append(question)
    assert not short_slots
    sets = []
    for item in imported['sets']:
        children = []
        ids = [r for r in imported['records'] if r['setId']==item['id']]
        for group in dict.fromkeys(r['subgroup'] for r in ids):
            label = ('Phần 1 · Hỏi–đáp ngắn' if group=='short' else 'Phần 2 · Trắc nghiệm') if item['id']=='tap-1' else f'Nhóm {group[1:]}'
            children.append({'id':f"{item['id']}-{group}",'title':label})
        sets.append(item|{'rawCount':len(ids),'uniqueCount':sum(item['id'] in q['setIds'] for q in questions),
                         'groups':children if len(children)>1 else []})
    result = {'course':{'id':'hcm-bank','name':'Tư tưởng Hồ Chí Minh'},'questionRevision':'v1',
              'questions':questions,'sets':sets,'sourceMap':source_map,
              'sourceOrder':{record['id']:index for index,record in enumerate(imported['records'])},
              'statistics':{'sourceOccurrences':261,'uniqueItems':len(questions),
                            'duplicateOccurrencesRemoved':261-len(questions),
                            'gradable':sum(q['kind']=='mcq' for q in questions),
                            'pending':sum(q['kind']=='pending' for q in questions),
                            'essays':sum(q['kind']=='essay' for q in questions),'generatedDistractorItems':23},
              'chapters':[],'examForms':[],'studySections':[],'docLines':[],'slidePages':[]}
    from extend_hcm_past_exam import extend
    from hcm_slide_sources import attach_bank, reviews
    extend(result, reviews())
    attach_bank(result)
    (ROOT/'dist/hcm-bank-data.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(result['statistics']))
    return result


if __name__ == '__main__':
    build()
