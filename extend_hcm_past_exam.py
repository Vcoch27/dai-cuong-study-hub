"""Preserve all 30 original exam positions; explicitly merge duplicates in All."""
import copy
import re
from pathlib import Path

ROOT=Path(__file__).parent
SET_ID='past-exam-1'
TITLE='Đề năm trước 1'
BIOGRAPHY='https://hochiminh.vn/book/cuoc-doi-su-nghiep/bien-nien-tieu-su-ho-chi-minh/ho-chi-minh-tieu-su-bao-tang-ho-chi-minh-nxb-chinh-tri-quoc-gia-ha-noi-nam-2008-20'
# Each entry is an explicit semantic comparison, not fuzzy string similarity.
DUPLICATES={1:'happiness-quote-ambiguous',2:'marx-self-emancipation',3:'subjective-factors',
5:'colonial-before-metropole',6:'three-communist-organizations',9:'definition-fill',
11:'departure-purpose',12:'colonial-nature-period',13:'japan-france-1940',15:'lenin-theses-work',
17:'duong-lectures',18:'not-hcm-work',19:'theoretical-sources',20:'duong-lectures',
22:'imperialist-context',23:'youth-league-place',24:'bourgeois-limit',25:'return-landmark',
26:'declaration-human-rights',27:'colonial-union-period',28:'three-formative-bases',29:'declaration-commitment'}
KEYS='? A A C B D B C B A A A C B D B A C D B D C A A B D B A B B'.split()
NEW={
4:('direct',[(2,31)],'Trang ghi luận cương đăng báo tháng 7/1920.',
   'Đáp án C: năm 1920, gắn bước ngoặt tìm thấy con đường giải phóng dân tộc qua luận cương của Lênin.'),
7:('context',[(2,30)],'Trang có hành trình Mỹ, Anh, Pháp nhưng không ghi sự kiện từ Anh trở lại Pháp năm 1917.',
   'Đáp án B: Pháp. Tiểu sử Bảo tàng Hồ Chí Minh xác nhận cuối năm 1917 Nguyễn Tất Thành từ Anh trở lại Pháp; chi tiết này không được ghi trực tiếp trên slide.'),
8:('direct',[(4,40),(3,5)],'Trang 4:40 có đúng đoạn Đảng cầm quyền trong Di chúc, bác bỏ việc gán cho Tuyên ngôn của Đảng Cộng sản; trang 3:5 đối chiếu lựa chọn A.',
   'Đáp án C là phát biểu sai. Đoạn về Đảng cầm quyền, cần kiệm liêm chính và người đầy tớ trung thành của nhân dân nằm trong Di chúc. Tuyên ngôn của Đảng Cộng sản là tác phẩm của C. Mác và Ph. Ăngghen, không phải tác phẩm của Hồ Chí Minh.'),
10:('context',[(2,28),(2,27)],'Sơ đồ cho khung 1941–1969 và trang 27 có các hoạt động sáng lập; slide không ghi đủ mốc thành lập từng tổ chức.',
    'Đáp án A: giai đoạn 1941–1969. Mặt trận Việt Minh ra đời năm 1941, Đội Việt Nam Tuyên truyền Giải phóng quân năm 1944. Hai sự kiện đều thuộc giai đoạn tư tưởng tiếp tục phát triển, hoàn thiện.'),
14:('context',[(2,28),(2,36)],'Có khung giai đoạn 1941–1969, nhưng không ghi sự kiện dùng tên Hồ Chí Minh năm 1942.',
    'Đáp án B sau khi chuẩn hóa ranh giới giai đoạn thành 29/1/1941–2/9/1969 theo sơ đồ bài học. Nguyễn Ái Quốc dùng tên Hồ Chí Minh khi sang Trung Quốc tháng 8/1942. Bản chép gốc của B bị sai các mốc đầu và cuối; bản gốc vẫn được giữ để đối chiếu.'),
16:('context',[(2,31),(3,16)],'Có tên luận cương và vai trò đối với con đường cứu nước; không có nguyên văn lời cảm thán trong câu hỏi.',
    'Đáp án B: Luận cương của Lênin về vấn đề dân tộc và thuộc địa. Không nhầm với Chủ nghĩa Tam dân hoặc các bản Tuyên ngôn Độc lập.'),
21:('none',[],'Không có mốc sang Anh năm 1913 trong bốn PDF.',
    'Đáp án D: năm 1913. Tiểu sử Bảo tàng Hồ Chí Minh ghi đầu năm 1913 Nguyễn Tất Thành rời Mỹ, trở về Lơ Havơrơ rồi sang Anh; không dùng năm 1917, là mốc từ Anh trở lại Pháp.'),
30:('none',[],'Không có địa danh nơi sinh chi tiết trong bốn PDF.',
    'Đáp án B: làng Chùa, tức Hoàng Trù, quê ngoại. Phân biệt với làng Sen là quê nội. Địa chỉ hành chính được giữ theo cách ghi lịch sử trong đề, không dùng làm địa chỉ hành chính hiện hành.'),
}


def parse():
    text=(ROOT/'content/hcm-bank/past-exam-1.txt').read_text(encoding='utf-8-sig')
    starts=list(re.finditer(r'^CÂU (\d+)([^\n]*)\n=+\s*\n',text,re.M))
    assert [int(m[1]) for m in starts]==list(range(1,31))
    records=[]
    for i,m in enumerate(starts):
        block=text[m.end():starts[i+1].start() if i+1<len(starts) else len(text)]
        block=re.split(r'\n=+',block)[0].strip()
        parts=re.split(r'(?m)^([ABCD])\.\s*',block)
        assert len(parts)==9 and parts[1::2]==list('ABCD'),m[1]
        records.append({'id':f'past1-{i+1:02}','setId':SET_ID,'setTitle':TITLE,'subgroup':'mcq',
            'document':7,'part':'mcq','number':i+1,'kind':'mcq',
            'question':re.sub(r'\s+',' ',parts[0]).strip(),
            'choices':[re.sub(r'\s+',' ',v).strip() for v in parts[2::2]],
            'providedAnswer':None,'page':None,
            'notes':([m[2].strip()] if m[2].strip() else [])})
    return records


def extend(data, review):
    originals={q['id']:q for q in data['questions']}
    records=parse()
    additions=[]
    for record,key in zip(records,KEYS):
        number=record['number']
        duplicate=originals.get('bank-'+DUPLICATES[number]) if number in DUPLICATES else None
        choices=record['choices'].copy()
        question=record['question']
        note='Bản chép không có khóa đáp án chính thức; đáp án do biên tập đối chiếu. '
        if record['notes']: note+='Câu gốc có ghi chú: '+'; '.join(record['notes'])+'. '
        if number==10: note+='Phương án D được bổ sung trong bản chép do ảnh bị cắt. '
        if number in (17,20):
            question+=' Đây là tác phẩm nào?'
            note+='Câu 17 và 20 trùng nội dung; giữ đủ vị trí trong đề, gộp trong Toàn bộ. '
        if number==14:
            choices[1]='Từ 29/1/1941 đến 2/9/1969'
            note+='Đã hiệu đính mốc giai đoạn của B; bản chép gốc được giữ bên dưới. '
        if number==19:
            question='Ba nhóm cơ sở lý luận hình thành tư tưởng Hồ Chí Minh được khái quát đúng là gì?'
            note+='Làm rõ tiêu chí ba nhóm để tránh đáp án A kể lặp chủ nghĩa yêu nước như một nhóm riêng. '
        if number==30: note+='Đề gốc cảnh báo địa danh mờ; đối chiếu tiểu sử chính thức để xác nhận làng Chùa (Hoàng Trù). '
        if duplicate:
            slide_review=copy.deepcopy(review[duplicate['id']])
            explanation=duplicate['explanation']
            # These explanations must refer to the original A–D order of this exam.
            if number==1: explanation='Các lựa chọn B, C, D có thể chồng lấn theo cấp độ khái quát. Trang 3:8 khẳng định độc lập gắn tự do, hạnh phúc của dân nhưng không tạo ra khóa chấm chính thức cho bốn phương án này. Giữ câu cần đối chiếu, không tự đoán đáp án.'
            if number==11: explanation='Trong bốn lựa chọn, A gần với ý định tìm hiểu Pháp và các nước để trở về giúp đồng bào. B và D gán nhận thức về con đường vô sản có sẵn từ năm 1911; C biến mục đích cứu nước thành tìm cuộc sống riêng. Ý định đầy đủ rộng hơn nội dung ngắn của A.'
            if number==12: explanation='Đáp án A: cuối 1920–đầu 1930, đối chiếu tiêu đề trang 32 và các luận điểm về bản chất thực dân ở trang 34. Trải nghiệm 1911–1920 là tiền đề; câu hỏi đang phân loại nội dung tư tưởng cơ bản theo hệ thời kỳ của bài học.'
            if number==19: explanation='Đáp án D khái quát đúng ba nhóm lý luận: truyền thống dân tộc, tinh hoa văn hóa nhân loại và chủ nghĩa Mác – Lênin. A tách chủ nghĩa yêu nước ra khỏi nhóm truyền thống, làm lặp cấp phân loại; B và C thiếu một nhóm.'
            references=copy.deepcopy(duplicate['source']['references'])
        else:
            status,refs,reason,explanation=NEW[number]
            slide_review={'status':status,'refs':refs,'reason':reason}
            references=[{'title':'Tiểu sử Hồ Chí Minh · Bảo tàng Hồ Chí Minh','url':BIOGRAPHY}]
        q={'id':f'bank-past1-q{number:02}','pastExam':True,'originalNumber':number,
           'duplicateOf':duplicate['id'] if duplicate else None,'kind':'pending' if key=='?' else 'mcq',
           'chapter':0,'question':question,'choices':choices,'answer':None if key=='?' else ord(key)-65,
           'explanation':explanation,'keyOrigin':'editorial' if key!='?' else 'pending',
           'generatedDistractors':False,'editorialNote':note.strip(),'setIds':[SET_ID],
           'groupIds':[SET_ID+'-mcq'],'occurrences':[record], '_slideReview':slide_review,
           'source':{'kind':'bank','label':f'{TITLE} · Câu {number:02}',
                     'evidence':'\n'.join([record['question']]+[f'{chr(65+i)}. {v}' for i,v in enumerate(record['choices'])]),
                     'references':references}}
        additions.append(q)
        canonical=duplicate or q
        if duplicate:
            canonical['occurrences'].append(copy.deepcopy(record))
            if SET_ID not in canonical['setIds']: canonical['setIds'].append(SET_ID)
            if SET_ID+'-mcq' not in canonical['groupIds']: canonical['groupIds'].append(SET_ID+'-mcq')
        data['sourceMap'][record['id']]=canonical['id']
        data['sourceOrder'][record['id']]=261+number-1
    data['questions'].extend(additions)
    data['sets'].append({'id':SET_ID,'title':TITLE,'description':'Giữ đủ 30 vị trí câu · Có câu phục dựng, hiệu đính; đáp án biên tập',
                         'rawCount':30,'uniqueCount':30,'groups':[],'preservePositions':True})
    unique=[q for q in data['questions'] if not q.get('duplicateOf')]
    data['statistics'].update({'sourceOccurrences':291,'uniqueItems':len(unique),'displayItems':len(data['questions']),
          'duplicateOccurrencesRemoved':291-len(unique), 'gradable':sum(q['kind']=='mcq' for q in unique),
          'pending':sum(q['kind']=='pending' for q in unique),'essays':sum(q['kind']=='essay' for q in unique)})
    assert len(data['questions'])==169 and len(unique)==147 and len(records)==30
