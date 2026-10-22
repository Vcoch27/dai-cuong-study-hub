"""Explicit decisions for canonical questions. Original source occurrences remain intact."""
ITEMS = []


def add(slug, sources, key, explanation, refs='', question=None, choices=None, note=None):
    ITEMS.append(dict(slug=slug,sources=sources.split(),key=key,explanation=explanation,
                      refs=refs.split(),question=question,choices=choices,note=note))


def short(slug,sources,wrongs,explanation,refs='',question=None):
    add(slug,sources,'provided',explanation,refs,question,wrongs)


short('october-1917','t1-short-01 t2-g1-15 t3-mcq-01 t6-mcq-21',
 ['Cách mạng tư sản Pháp năm 1789','Cách mạng Tân Hợi năm 1911','Cách mạng tháng Tám Việt Nam năm 1945'],
 'Sự kiện được nhắc đến là Cách mạng Tháng Mười Nga năm 1917, cần phân biệt với các cuộc cách mạng dân chủ tư sản và Cách mạng tháng Tám.','s2p5')
short('declaration-commitment','t1-short-02 t2-g1-19 t3-mcq-02 t4-mcq-33 t5-mcq-01 t6-mcq-08',
 ['Tất cả ý chí và sức mạnh, lòng dũng cảm và tinh thần đoàn kết','Tất cả trí tuệ và tài năng, công sức và thành quả của dân tộc','Tất cả tinh thần yêu nước, niềm tin và truyền thống đấu tranh'],
 'Cụm từ đầy đủ trong Tuyên ngôn Độc lập gồm cả tinh thần, lực lượng, tính mạng và của cải; không thay bằng những cụm gần nghĩa.')
short('father-phobang-year','t1-short-03 t2-g1-04 t3-mcq-03 t6-mcq-13',['1895','1900','1906'],
 'Nguyễn Sinh Sắc đỗ Phó bảng khoa Tân Sửu năm 1901. Đây là câu hỏi về năm, khác với câu hỏi xác định học vị.','biography')
short('first-home-visit','t1-short-04 t2-g1-11 t3-mcq-05 t6-mcq-11',['1954','1956','1961'],
 'Lần đầu Hồ Chí Minh về thăm quê sau khi trở thành Chủ tịch nước là năm 1957; năm 1961 là lần về thăm sau.','home')
short('maternal-village','t1-short-05 t2-g1-02 t3-mcq-06 t5-mcq-02 t6-mcq-14',
 ['Làng Sen (Kim Liên), huyện Nam Đàn, tỉnh Nghệ An','Làng Dương Nỗ, huyện Phú Vang, tỉnh Thừa Thiên Huế','Làng Trù Sơn, huyện Đô Lương, tỉnh Nghệ An'],
 'Quê ngoại là làng Hoàng Trù, còn gọi là làng Chùa; làng Sen là quê nội. Địa danh hành chính trong câu được giữ theo tư liệu lịch sử.','biography')
short('marxist-nature','t1-short-06 t2-g1-14 t3-mcq-07 t5-mcq-04 t6-mcq-09',
 ['Giá trị văn hóa truyền thống Việt Nam','Tinh hoa văn hóa phương Đông','Tư tưởng dân chủ văn hóa phương Tây'],
 'Chủ nghĩa Mác – Lênin quyết định bản chất khoa học và cách mạng; truyền thống dân tộc và văn hóa nhân loại là những nguồn ảnh hưởng khác.')
short('subjective-factors','t1-short-07 t1-mcq-21 t2-g1-08 t3-mcq-08 t3-mcq-44 t6-mcq-23',
 ['Phẩm chất cá nhân Hồ Chí Minh; truyền thống gia đình, quê hương và văn hóa dân tộc',
  'Tài năng hoạt động thực tiễn; truyền thống dân tộc và tinh hoa văn hóa nhân loại',
  'Phẩm chất cá nhân Hồ Chí Minh; phong trào dân tộc và bối cảnh chính trị thế giới'],
 'Nhân tố chủ quan gồm phẩm chất cá nhân và tài năng hoạt động, tổng kết thực tiễn, phát triển lý luận. Các nguồn văn hóa, truyền thống và bối cảnh không thay thế hai mặt đó.','s2p23 s2p27')
short('sacred-rights','t1-short-08 t2-g1-23 t3-mcq-09 t6-mcq-24',
 ['Quyền tự trị và hợp tác quốc tế','Quyền tham gia các tổ chức quốc tế','Quyền giao thương và phát triển kinh tế'],
 'Đáp án nguồn là quyền độc lập, tự do, bình đẳng của dân tộc; quyền giao thương hay tham gia tổ chức không thay cho quyền dân tộc cơ bản.')
short('departure-baggage','t1-short-09 t2-g1-12 t3-mcq-10 t6-mcq-12',
 ['Chủ nghĩa Mác – Lênin và đường lối cách mạng vô sản','Tư tưởng dân chủ tư sản và mô hình quân chủ lập hiến','Chủ nghĩa Tam dân và mô hình nhà nước dân chủ tư sản'],
 'Trước khi ra đi, hành trang là lòng yêu nước và truyền thống dân tộc; việc tìm đến con đường cách mạng vô sản là kết quả của quá trình về sau.','s2p29')
short('proletarian-path','t1-short-10 t2-g1-21 t2-g3-05 t3-mcq-11 t5-mcq-07 t6-mcq-18',
 ['Cách mạng tư sản','Cải cách dân chủ tư sản','Cách mạng phong kiến'],
 'Con đường được xác định là cách mạng vô sản; cần phân biệt con đường này với các khuynh hướng cứu nước tư sản hoặc phong kiến.','s2p34')
short('duc-thanh-teacher','t1-short-11 t2-g1-16 t3-mcq-12 t6-mcq-10',
 ['Trường Quốc học ở Huế','Trường Pháp–Việt Đông Ba ở Huế','Trường Pháp–bản xứ ở Vinh'],
 'Dục Thanh ở Phan Thiết là nơi Nguyễn Tất Thành dạy học. Các trường khác trong lựa chọn gắn với thời kỳ học tập.','s2p29')
short('creative-marxism','t1-short-12 t2-g1-03 t3-mcq-13 t4-mcq-09 t6-mcq-25',
 ['Vận dụng kinh nghiệm cách mạng tư sản vào hoàn cảnh của Việt Nam','Kế thừa hệ thống tư tưởng Nho giáo để xây dựng đường lối cách mạng','Phát triển chủ nghĩa Tam dân thành đường lối cách mạng Việt Nam'],
 'Nền tảng là vận dụng và phát triển sáng tạo chủ nghĩa Mác – Lênin trong điều kiện cụ thể Việt Nam, không thay bằng một nguồn tư tưởng khác.','s1p2')
short('nguyen-ai-quoc-name','t1-short-13 t2-g1-22 t3-mcq-15 t4-mcq-06 t5-mcq-06 t6-mcq-03',
 ['Khi rời bến cảng Nhà Rồng năm 1911','Khi tham gia Đại hội Tua tại Pháp năm 1920','Khi sang Liên Xô hoạt động vào năm 1923'],
 'Tên Nguyễn Ái Quốc xuất hiện khi gửi Yêu sách của nhân dân An Nam đến Hội nghị Vécxây năm 1919.','biography')
short('colonial-union-period','t1-short-14 t2-g1-13 t3-mcq-16 t6-mcq-07',
 ['Giai đoạn trước khi ra đi tìm đường cứu nước năm 1911','Giai đoạn tìm con đường cứu nước từ năm 1911 đến năm 1920','Giai đoạn bảo vệ đường lối cách mạng từ năm 1930 đến năm 1941'],
 'Hội Liên hiệp thuộc địa được thành lập năm 1921, thuộc giai đoạn hình thành nội dung cơ bản về cách mạng Việt Nam.','biography s2p32')
short('became-communist','t1-short-15 t2-g2-19',
 ['Khi gửi Yêu sách tới Hội nghị Vécxây năm 1919','Khi tham gia Hội Liên hiệp thuộc địa tại Pháp năm 1921','Khi chủ trì hợp nhất các tổ chức cộng sản ở Việt Nam năm 1930'],
 'Bước chuyển được đánh dấu ở Đại hội Tua tháng 12/1920: tán thành Quốc tế III, tham gia thành lập Đảng Cộng sản Pháp.','s2p31')
short('traditional-values','t1-short-16 t2-g1-10 t3-mcq-17 t6-mcq-04',
 ['Chủ nghĩa yêu nước; dân chủ phương Tây; tinh thần nhân ái, khoan dung của dân tộc',
  'Tinh thần đoàn kết cộng đồng; phép biện chứng duy vật; tư tưởng nhân nghĩa, bao dung',
  'Truyền thống yêu nước; tư tưởng Tam dân; các giá trị tự do và bình đẳng phương Tây'],
 'Nhóm được hỏi là giá trị truyền thống dân tộc: yêu nước, đoàn kết cộng đồng, nhân ái và bao dung. Các phương án nhiễu trộn thêm nguồn lý luận hoặc văn hóa khác.','s2p8 s2p9 s2p11')
short('youth-league-place','t1-short-17 t2-g1-18 t3-mcq-18 t6-mcq-05',['Pháp','Liên Xô','Thái Lan'],
 'Hội Việt Nam Cách mạng Thanh niên được thành lập tại Quảng Châu, Trung Quốc năm 1925.','biography')
short('basic-thought-period','t1-short-18 t2-g1-17 t3-mcq-19 t4-mcq-25 t5-mcq-03 t6-mcq-22',
 ['Từ trước năm 1911 đến khi ra đi tìm đường cứu nước','Từ năm 1911 đến cuối năm 1920','Từ đầu năm 1930 đến đầu năm 1941'],
 'Cuối năm 1920–đầu năm 1930 là giai đoạn hình thành những nội dung cơ bản về cách mạng Việt Nam. Không nhầm với giai đoạn tìm đường hoặc bảo vệ đường lối.','s2p28 s2p32')
short('period-1911-1920','t1-short-19 t2-g1-20 t3-mcq-20 t6-mcq-16',
 ['Hình thành tư tưởng yêu nước, chí hướng cứu nước mới trước khi đi ra nước ngoài',
  'Hình thành nội dung cơ bản về cách mạng Việt Nam và chuẩn bị thành lập Đảng',
  'Giữ vững đường lối cách mạng Việt Nam trong thử thách sau khi Đảng ra đời'],
 'Nội dung đặc trưng là tìm ra con đường cứu nước, giải phóng dân tộc Việt Nam theo cách mạng vô sản. Các mô tả khác thuộc giai đoạn trước 1911, 1921–1930 hoặc 1930–1941.','s2p30')
short('patriotism-first','t1-short-20 t4-mcq-01 t5-mcq-12',['Truyền thống hiếu học','Tinh thần nhân ái','Tính gắn bó cộng đồng'],
 'Trong hệ giá trị truyền thống, chủ nghĩa yêu nước giữ vai trò hàng đầu, tạo động lực tìm con đường cứu nước.')
short('lenin-reading-country','t1-short-21 t2-g1-25 t3-mcq-25 t6-mcq-20',['Trung Quốc','Liên Xô','Anh'],
 'Nguyễn Ái Quốc đọc Luận cương của Lênin ở Pháp năm 1920, không phải ở Liên Xô hay Trung Quốc.','s2p31 biography')
short('will-start-year','t1-short-22 t4-mcq-11 t5-mcq-15',['1960','1968','1969'],
 'Hồ Chí Minh bắt đầu viết Di chúc ngày 10/5/1965; các năm sau là thời gian bổ sung, sửa chữa hoặc công bố.','will')
short('departure-year','t2-g2-00',['1905','1919','1920'],
 'Nguyễn Tất Thành rời bến Nhà Rồng ngày 5/6/1911 để tìm đường cứu nước.','biography')

add('party-foundation','t1-mcq-01 t3-mcq-26','D','Nền tảng tư tưởng và kim chỉ nam gồm cả chủ nghĩa Mác – Lênin và tư tưởng Hồ Chí Minh.','',question='Đảng Cộng sản Việt Nam lấy những hệ tư tưởng nào làm nền tảng tư tưởng, kim chỉ nam cho hành động?')
add('colonial-before-metropole','t1-mcq-02 t3-mcq-27 t4-mcq-31','D','Cách mạng thuộc địa có thể chủ động giành thắng lợi trước cách mạng vô sản ở chính quốc; không lệ thuộc vào sự thắng lợi đồng thời.','',question='Nhận định nào đúng về khả năng thắng lợi của cách mạng giải phóng dân tộc ở thuộc địa so với cách mạng vô sản ở chính quốc?')
add('versailles-date','t1-mcq-03 t3-mcq-28','C','Yêu sách của nhân dân An Nam được gửi đến Hội nghị Vécxây ngày 18/6/1919.','biography')
add('hue-family-visits','t1-mcq-04 t3-mcq-29','A','Gia đình Nguyễn Sinh Cung vào Huế hai lần, năm 1895 và năm 1906.','biography',choices=['2','3','1','4'])
add('colonial-nature-period','t1-mcq-05 t3-mcq-30','D','Sự khái quát bản chất, thủ đoạn của chủ nghĩa thực dân thành nội dung tư tưởng cơ bản gắn với giai đoạn 1921–1930; cần phân biệt với trải nghiệm tìm đường trước đó.','s2p32 s2p34',choices=['1911–1920','1930–1941','Trước năm 1911','1921–1930'])
add('return-landmark','t1-mcq-06 t3-mcq-31 t5-mcq-11','D','Người trở về qua cột mốc 108 ở khu vực Pác Bó, Trường Hà, Hà Quảng, Cao Bằng. Pác Bó không phải tên tỉnh. Địa danh giữ theo giai đoạn lịch sử.','biography')
add('imperialist-context','t1-mcq-07 t3-mcq-32','C','Bối cảnh là chủ nghĩa tư bản chuyển từ tự do cạnh tranh sang đế quốc chủ nghĩa.','s2p5 s2p6')
add('not-hcm-work','t1-mcq-08 t2-g1-24 t3-mcq-24 t3-mcq-33 t6-mcq-19','A','Tuyên ngôn của Đảng Cộng sản là tác phẩm của C. Mác và Ph. Ăngghen, không phải của Hồ Chí Minh.')
add('lenin-theses-work','t1-mcq-09 t3-mcq-34 t4-mcq-29','C','Bản Sơ thảo của Lênin về dân tộc và thuộc địa giúp Nguyễn Ái Quốc tìm ra con đường giải phóng dân tộc.','s2p31')
add('three-communist-organizations','t1-mcq-10 t3-mcq-35','A','Ba tổ chức là Đông Dương Cộng sản Đảng, An Nam Cộng sản Đảng và Đông Dương Cộng sản Liên đoàn; Hội Thanh niên không phải tổ chức cộng sản thứ tư. Hội nghị đầu 1930 hợp nhất hai tổ chức đầu, Liên đoàn được chấp nhận gia nhập sau đó.')
add('departure-purpose','t1-mcq-11 t3-mcq-36','C','Khi ra đi năm 1911, Nguyễn Tất Thành muốn tìm hiểu phương Tây để tìm đường giúp đồng bào; chưa phải đã chọn sẵn cách mạng vô sản.','s2p29')
add('bourgeois-limit','t1-mcq-12 t3-mcq-37','D','Người nhận thấy các cuộc cách mạng tư sản chưa giải phóng triệt để quần chúng lao động, nên gọi là cách mạng chưa đến nơi.')
add('theoretical-sources','t1-mcq-13 t3-mcq-38','B','Ba nhóm cơ sở lý luận là truyền thống dân tộc, tinh hoa văn hóa nhân loại và chủ nghĩa Mác – Lênin. Chủ nghĩa yêu nước nằm trong truyền thống dân tộc, không là nhóm thứ tư.','s2p8 s2p13 s2p21')
add('liberation-conditions','t1-mcq-14 t3-mcq-39','D','Phương án đầy đủ kết hợp sự tự nỗ lực của dân tộc, sự giúp đỡ quốc tế và lãnh đạo của Đảng; các phương án khác thiếu hoặc phủ nhận một mặt.')
add('eulogy-reader','t1-mcq-15 t2-g1-06 t3-mcq-04 t3-mcq-40 t6-mcq-15','B','Lê Duẩn đọc điếu văn tại lễ truy điệu ngày 9/9/1969.','s2p46')
add('national-task-first','t1-mcq-16 t2-g3-24 t3-mcq-41','A','Trong cách mạng thuộc địa, giải phóng dân tộc được đặt lên hàng đầu, gắn với lập trường giai cấp công nhân.','s2p35')
add('happiness-quote-ambiguous','t1-mcq-17 t3-mcq-42','?', 'Câu hỏi không nêu tiêu chí chọn: hạnh phúc nhân dân, nội dung độc lập dân tộc và quan hệ độc lập–CNXH đều có thể được liên hệ từ đoạn trích. Cần đáp án hoặc tiêu chí chấm của đề gốc.',note='Nhiều phương án có thể đúng theo các mức khái quát; không gán một đáp án để chấm tự động.')
add('definition-fill','t1-mcq-18 t3-mcq-43','A','Ba phần khớp với định nghĩa là toàn diện và sâu sắc; cách mạng Việt Nam; giá trị truyền thống.','s1p2',question='Điền ba cụm còn thiếu: Tư tưởng Hồ Chí Minh là hệ thống quan điểm (1) về những vấn đề cơ bản của (2), kế thừa và phát triển các (3) tốt đẹp của dân tộc.',choices=['Toàn diện và sâu sắc; cách mạng Việt Nam; giá trị truyền thống','Lý luận; cách mạng Việt Nam; giá trị truyền thống','Toàn diện và sâu sắc; Hồ Chí Minh; giá trị truyền thống','Lý luận; Hồ Chí Minh; giá trị truyền thống'],note='Khôi phục ba chỗ trống bị lỗi trong bản trích; bản gốc vẫn được lưu bên cạnh.')
add('marx-self-emancipation','t1-mcq-22 t3-mcq-45','B','Luận điểm về sự tự giải phóng của giai cấp công nhân thuộc C. Mác; các câu còn lại gắn với cách Hồ Chí Minh diễn đạt tinh thần tự lực.')
add('father-death-place','t1-mcq-24 t3-mcq-46','A','Nguyễn Sinh Sắc qua đời tại Cao Lãnh, nay thuộc Đồng Tháp. Tên địa phương được hiểu theo tư liệu lịch sử.','father')
add('party-before-revolution','t1-mcq-25 t3-mcq-47','B','Đường Kách mệnh nêu cách mạng trước hết phải có đảng cách mệnh để vận động, tổ chức trong nước và liên lạc quốc tế.')
add('nothing-precious-work','t2-g1-05 t3-mcq-14 t5-mcq-09 t6-mcq-02','A','Câu Không có gì quý hơn độc lập, tự do nằm trong Lời kêu gọi đồng bào và chiến sĩ cả nước ngày 17/7/1966, khác Lời kêu gọi toàn quốc kháng chiến năm 1946.','independence1966')
add('personal-qualities','t2-g1-07 t3-mcq-22 t6-mcq-01','D','Bốn nhóm phẩm chất gồm hoài bão, lý tưởng; tư duy độc lập sáng tạo nhạy bén; kiên cường bất khuất; trái tim nhân ái.','s2p23')
add('definition-congress-xi','t2-g1-09 t3-mcq-23 t6-mcq-17','B','Định nghĩa với nội dung tài sản tinh thần to lớn, quý giá và mãi mãi soi đường được nêu tại Đại hội XI năm 2011; không nhầm mốc khẳng định nền tảng tư tưởng ở Đại hội VII.','partyconcept')
add('petition-eight-points','t2-g2-01','D','Yêu sách của nhân dân An Nam năm 1919 gồm tám điểm.','biography',question='Bản Yêu sách của nhân dân An Nam gửi Hội nghị Vécxây năm 1919 gồm bao nhiêu điểm?')
add('method-party-science','t2-g2-02','B','Thống nhất tính đảng và tính khoa học là một yêu cầu phương pháp luận của môn học.','s1p4')
add('indictment-year','t2-g2-03','A','Bản án chế độ thực dân Pháp xuất bản lần đầu năm 1925.','s2p32')
add('marx-dialectic','t2-g2-04 t4-mcq-23','A','Hồ Chí Minh nhấn mạnh ưu điểm phương pháp làm việc biện chứng của chủ nghĩa Mác.','s2p13')
add('duong-year','t2-g2-05','A','Đường Kách mệnh được xuất bản năm 1927, khác Bản án chế độ thực dân Pháp năm 1925.','s2p32')
add('youth-league-year','t2-g2-10 t4-mcq-02','A','Hội Việt Nam Cách mạng Thanh niên được thành lập tháng 6/1925 tại Quảng Châu.','biography')
add('return-date','t2-g2-11','D','Nguyễn Ái Quốc trở về Tổ quốc ngày 28/1/1941.','s2p35')
add('plenum-eight','t2-g2-13','B','Hội nghị Trung ương lần thứ tám tháng 5/1941 do Nguyễn Ái Quốc chủ trì hoàn chỉnh chuyển hướng chiến lược giải phóng dân tộc.','biography')
add('socialist-party-year','t2-g2-16','B','Mốc được sử dụng theo tiểu sử chính thức và lời Hồ Chí Minh kể lại là năm 1919; không nhầm với gia nhập Đảng Cộng sản Pháp cuối năm 1920.','socialistparty',choices=['1921','1919','1918','1920'])
add('three-peoples','t2-g2-17','B','Nội dung Tam dân là dân tộc độc lập, dân quyền tự do, dân sinh hạnh phúc; không phải một kỹ thuật phương pháp cách mạng chung.')
add('party-foundation-congress','t2-g2-18 t3-mcq-53 t4-mcq-17','C','Đại hội VII năm 1991 lần đầu khẳng định cả chủ nghĩa Mác – Lênin và tư tưởng Hồ Chí Minh là nền tảng tư tưởng, kim chỉ nam.','partyconcept')
add('subject-of-study','t2-g2-21','B','Đối tượng gồm hệ thống quan điểm về cách mạng Việt Nam và quá trình vận động, hiện thực hóa; quy luật chung của tự nhiên, xã hội hay tư duy không phải đối tượng riêng của môn học.','s1p3')
add('indictment-place','t2-g2-22 t4-mcq-35','C','Bản án chế độ thực dân Pháp được xuất bản ở Pháp; Đường Kách mệnh được xuất bản tại Trung Quốc.','biography')
add('basis-ambiguous','t2-g2-24','?','Câu hỏi không xác định cơ sở lý luận, thực tiễn hay cơ sở dân tộc. Nhiều nguồn ảnh hưởng trong các lựa chọn đều liên quan đến hình thành tư tưởng, nên chưa đủ tiêu chí chọn một.',note='Thiếu phạm vi của câu dẫn; cần đối chiếu đề hoặc đáp án của giảng viên.')
add('patriotic-trend-count','t2-g2-26','B','Hai khuynh hướng cứu nước trước khi con đường vô sản được xác lập là phong kiến và dân chủ tư sản.','s2p2',choices=['Một khuynh hướng','Hai khuynh hướng','Ba khuynh hướng','Bốn khuynh hướng'])
add('religion-influence','t2-g2-28','D','Trong nhóm nguồn ảnh hưởng được trình bày, có Nho giáo, Phật giáo, Tam dân; Hồi giáo không nằm trong nhóm được nêu. Không diễn giải thành khẳng định tuyệt đối về mọi tiếp xúc trong đời Người.','s2p13')
add('french-communist-party-year','t2-g2-29','C','Nguyễn Ái Quốc tham gia sáng lập Đảng Cộng sản Pháp cuối năm 1920.','s2p31')
add('five-periods','t2-g2-34 t4-mcq-18','B','Năm thời kỳ theo cách phân kỳ của môn học: trước 1911, 1911–1920, 1921–1930, 1930–1941 và 1941–1969.','s2p28')
add('soviet-1923-1924','t2-g2-40','B','Giai đoạn 1923–1924 Nguyễn Ái Quốc hoạt động ở Liên Xô, trước chặng Trung Quốc.','s2p32')
add('patriotic-two-trends','t2-g2-42','B','Hai khuynh hướng phong kiến và dân chủ tư sản phản ánh các phong trào cứu nước trước khi con đường vô sản được xác lập.','s2p2')
add('colonial-union-year','t2-g2-43','B','Hội Liên hiệp thuộc địa được thành lập năm 1921; phân biệt với báo Người cùng khổ ra đời năm 1922.','biography')
add('duong-place','t2-g2-45','D','Đường Kách mệnh được xuất bản tại Quảng Châu, Trung Quốc năm 1927.','biography')
add('armed-uprising-form','t2-g3-01','C','Hình thái khởi nghĩa vũ trang toàn dân bao quát lực lượng nhân dân, không thu hẹp vào một bộ phận quân sự.')
add('nation-beneficiaries','t2-g3-03','C','Mục tiêu cấp thiết của giải phóng dân tộc hướng đến quyền lợi của toàn dân tộc, không thu hẹp trong một giai cấp.','s2p34')
add('colonial-contradiction','t2-g3-04','D','Mâu thuẫn chủ yếu là giữa dân tộc Việt Nam với thực dân Pháp và tay sai; không nhầm với mâu thuẫn nông dân–địa chủ.','s2p4')
add('territorial-independence','t2-g3-06','A','Độc lập về lãnh thổ gắn với thống nhất và toàn vẹn lãnh thổ quốc gia.')
add('self-emancipation','t2-g3-07','C','Tự nỗ lực giải phóng là yếu tố chủ thể. Sự giúp đỡ quốc tế quan trọng nhưng không thay được hành động của nhân dân thuộc địa.')
add('proletarian-leader','t2-g3-08','D','Lực lượng lãnh đạo là giai cấp công nhân thông qua đội tiên phong Đảng Cộng sản; liên minh công nông là lực lượng nền tảng.','s2p34')
add('worker-peasant-driving-force','t2-g3-09','B','Công nhân và nông dân là lực lượng động lực, nền tảng của cách mạng giải phóng dân tộc; không đồng nhất với lực lượng lãnh đạo.','s2p34')
add('revolutionary-violence','t2-g3-10 t4-mcq-27','A','Phương pháp là bạo lực cách mạng của quần chúng, khác bạo loạn hay ám sát cá nhân; gồm sự kết hợp chính trị và vũ trang.')
add('first-program-objectives','t2-g3-11','C','Những mục tiêu đánh đổ đế quốc và phong kiến, làm nước Nam độc lập thuộc Cương lĩnh chính trị đầu tiên năm 1930.')
add('violence-forces','t2-g3-12','C','Lực lượng tiến hành bạo lực cách mạng gồm lực lượng chính trị quần chúng và lực lượng vũ trang, không phải một loại đơn lẻ.')
add('independence-meaning','t2-g3-19','D','Độc lập phải gắn với đời sống ấm no, hạnh phúc của nhân dân, không thu hẹp quyền hưởng lợi cho một giai cấp hay liên minh.')
add('declaration-writing-place','t2-g3-20','A','Hồ Chí Minh viết Tuyên ngôn Độc lập tại Hà Nội, gắn với ngôi nhà 48 Hàng Ngang.')
add('violence-methods','t2-g3-21','B','Phương thức kết hợp đấu tranh chính trị với đấu tranh quân sự; phân biệt phương thức đấu tranh với tên một lực lượng.')
add('revolutions-compared','t2-g3-23','D','Người khảo nghiệm cách mạng Mỹ, Pháp và Nga để lựa chọn con đường cách mạng cho Việt Nam.')
add('class-standpoint','t2-g3-25','D','Hồ Chí Minh giải quyết vấn đề dân tộc trên lập trường giai cấp công nhân, kết hợp lợi ích giai cấp với lợi ích dân tộc.')
add('political-independence','t2-g3-28','B','Độc lập về chính trị gắn với quyền tự quyết dân tộc; không đồng nhất với riêng một nhiệm vụ sở hữu hoặc giải phóng cá nhân.')
add('declaration-year','t2-g3-29','A','Tuyên ngôn Độc lập được viết và công bố năm 1945.','s2p36')
add('declaration-human-rights','t3-mcq-48','B','Tuyên ngôn Độc lập là văn kiện đặt quyền con người và quyền dân tộc trong mối liên hệ trực tiếp.')
add('thailand-arrival','t3-mcq-49','B','Nguyễn Ái Quốc đến Xiêm, nay là Thái Lan, năm 1928.','s2p32 biography')
add('tam-tam-year','t3-mcq-50','B','Tâm Tâm Xã được thành lập năm 1923 ở Quảng Châu; không nhầm với Hội Việt Nam Cách mạng Thanh niên năm 1925.')
add('ly-thuy-name','t3-mcq-51','C','Người dùng tên Lý Thụy khi đến Quảng Châu, Trung Quốc vào tháng 11/1924.','biography',choices=['Khi sang Liên Xô tháng 6/1923','Khi hoạt động ở Thái Lan năm 1928','Khi đến Quảng Châu, Trung Quốc tháng 11/1924','Khi gửi Yêu sách đến Vécxây tháng 6/1919'],note='Sửa tên và ký tự II thành tháng 11; không suy đoán thêm ngày nếu bản trích không rõ.')
add('japan-france-1940','t3-mcq-52','D','Cặp cần điền trong Tuyên ngôn Độc lập là Nhật–Pháp: từ mùa thu 1940 thuộc địa của Nhật chứ không phải của Pháp nữa.')
add('declaration-colonial-crimes','t3-mcq-54','D','Đoạn tố cáo các chính sách thực dân được trích từ Tuyên ngôn Độc lập năm 1945.')
add('french-motto-school','t3-mcq-55','A','Nguyễn Tất Thành tiếp xúc khẩu hiệu Tự do–Bình đẳng–Bác ái khi học ở trường Pháp–bản xứ tại Vinh năm 1905, trước khi ra đi năm 1911.','biography')
add('three-formative-bases','t3-mcq-56','B','Cách phân nhóm được dùng là cơ sở thực tiễn, cơ sở lý luận và nhân tố chủ quan.','s2p2 s2p8 s2p23',choices=['2','3','1','4'])
add('many-translations-ambiguous','t3-mcq-57','?','Nhiều tác phẩm trong bốn lựa chọn đã được dịch sang nhiều ngôn ngữ. Câu dẫn không quy định ngôn ngữ, số bản dịch hay thể loại để có đáp án duy nhất.',note='Không dùng mức độ nổi tiếng của tác phẩm để đoán đáp án dự kiến của đề.')
add('childhood-name','t4-mcq-03','C','Tên thời niên thiếu là Nguyễn Sinh Cung; Nguyễn Tất Thành, Văn Ba và Nguyễn Ái Quốc gắn với những thời điểm khác.','biography')
add('eastern-culture-exception','t4-mcq-04','A','Thời kỳ Phục hưng thuộc nguồn văn hóa phương Tây. Nho giáo, Phật giáo và Tam dân được đặt trong nguồn ảnh hưởng phương Đông.')
add('schools-attended','t4-mcq-05','C','Nguyễn Tất Thành từng học Đông Ba và Quốc học Huế; Dục Thanh là nơi dạy học. Đã làm rõ các cặp trường để tránh lựa chọn mơ hồ.','biography',question='Cặp trường nào Nguyễn Tất Thành từng học, phân biệt với Dục Thanh là nơi Người dạy học?',choices=['Quốc học Huế và Dục Thanh','Đông Ba và Dục Thanh','Pháp–Việt Đông Ba và Quốc học Huế','Dục Thanh và Pháp–bản xứ Vinh'],note='Chuẩn hóa các lựa chọn gốc bị trùng hoặc thiếu tên trường; giữ nguyên câu gốc trong nguồn.')
add('chosen-path','t4-mcq-07','B','Con đường được xác định là độc lập dân tộc gắn liền với chủ nghĩa xã hội.','s1p6')
add('official-term-year','t4-mcq-08','B','Mốc chính thức gắn với Đại hội VII năm 1991; không nhầm với các định nghĩa được phát triển ở Đại hội IX và XI.','partyconcept')
add('socialism-builders','t4-mcq-10','C','Chủ thể xây dựng CNXH là nhân dân; công nhân, nông dân và trí thức đều là bộ phận của nhân dân.')
add('socialist-person','t4-mcq-12','C','Muốn xây dựng CNXH trước hết cần có con người xã hội chủ nghĩa; đây là khái niệm bao quát hơn từng phẩm chất riêng lẻ.')
add('wrong-marxist-learning','t4-mcq-13','D','Học Mác – Lênin phải để vận dụng lập trường, quan điểm và phương pháp vào thực tiễn, không đồng nhất với thuộc lòng sách.','s2p22')
add('socialism-general-goal','t4-mcq-14','D','Mục tiêu tổng quát hướng đến nâng cao đời sống nhân dân; phát triển sản xuất, khoa học kỹ thuật và kinh tế là những mặt phục vụ mục tiêu.')
add('democratic-centralism','t4-mcq-15','A','Tập trung dân chủ là nguyên tắc tổ chức cơ bản. Các nguyên tắc và quan hệ khác có vai trò riêng trong xây dựng Đảng.')
add('cadres-good-poor','t4-mcq-16','B','Cụm từ đúng là cán bộ tốt hay kém, cần nhớ đúng lời dẫn thay vì thay bằng từ gần nghĩa.','cadres')
add('eulogy-document','t4-mcq-19','D','Đoạn văn nằm trong Điếu văn của Ban Chấp hành Trung ương Đảng Lao động Việt Nam đọc tại lễ truy điệu ngày 9/9/1969.','s2p46')
add('unesco-description','t4-mcq-20','C','Cách diễn đạt trong nghị quyết UNESCO là anh hùng giải phóng dân tộc và nhà văn hóa kiệt xuất của Việt Nam; cần phân biệt với những cách gọi mở rộng trong các lựa chọn.','unesco',question='Nghị quyết UNESCO năm 1987 ghi nhận Hồ Chí Minh bằng cách diễn đạt nào?',note='Làm rõ tiêu chí là cách diễn đạt của UNESCO, thay cho câu dẫn gốc chỉ yêu cầu chọn đúng nhất.')
add('confucius-merit','t4-mcq-21','B','Ưu điểm được Hồ Chí Minh nêu ở học thuyết Khổng Tử là sự tu dưỡng đạo đức cá nhân.','s2p13')
add('national-question-substance','t4-mcq-22','D','Ở thuộc địa, thực chất vấn đề dân tộc trước hết là đấu tranh giải phóng dân tộc. Không đồng nhất với việc giành quyền lợi riêng cho một giai cấp.')
add('unity-mother-point','t4-mcq-24','C','Hồ Chí Minh gọi đoàn kết là điểm mẹ: làm tốt sẽ tạo điều kiện giải quyết những việc khác.','unity')
add('long-resistance','t4-mcq-26','B','Cụm khẩu hiệu đầy đủ là Trường kỳ kháng chiến, nhất định thắng lợi.','resistance',question='Hoàn chỉnh khẩu hiệu của Hồ Chí Minh: “Trường kỳ kháng chiến, …”?')
add('thought-scope','t4-mcq-28','C','Tư tưởng bao quát cách mạng dân tộc dân chủ nhân dân và cách mạng xã hội chủ nghĩa, không giới hạn vào một giai đoạn.','s1p2')
add('nothing-precious-year','t4-mcq-30','B','Lời kêu gọi chứa câu Không có gì quý hơn độc lập, tự do được công bố năm 1966.','independence1966')
add('our-strength-quote','t4-mcq-32','C','Cụm từ cần điền là đem sức ta, thể hiện tinh thần tự lực, chủ động tự giải phóng.')
add('individualism-warning','t4-mcq-34','A','Đoạn cảnh báo nói đến sa vào chủ nghĩa cá nhân, không phải thay bằng một biểu hiện riêng như hám danh hoặc tham ô.')
add('resistance-call-date','t4-mcq-36','B','Lời kêu gọi toàn quốc kháng chiến được ban hành ngày 19/12/1946.')
add('genuine-nationalism','t4-mcq-37','B','Chủ nghĩa dân tộc chân chính có giá trị động lực trong giải phóng thuộc địa, khác sô vanh hay dân tộc vị kỷ.')
add('empty-theory','t4-mcq-38','B','Cụm được dùng là lý luận suông khi lý luận tách rời thực tiễn.','s1p4')
add('imperialist-two-leeches','t4-mcq-39','C','Hai vòi của hình ảnh con đỉa gắn với sự bóc lột ở chính quốc và thuộc địa, đòi hỏi kết hợp đấu tranh ở cả hai nơi.')
add('human-motivation','t4-mcq-40','C','Con người là động lực quan trọng nhất; tài nguyên, vốn và khoa học kỹ thuật không thay thế vai trò chủ thể con người.','human')
add('peoples-resources','t4-mcq-41','D','Giải pháp nhấn mạnh huy động tài dân, sức dân, của dân để làm lợi cho dân dưới sự lãnh đạo của Đảng.','human')
add('party-political-line','t4-mcq-42','B','Xây dựng đường lối chính trị đúng đắn là vấn đề cốt tử của xây dựng Đảng về chính trị.')
add('will-unity','t4-mcq-43','C','Lời căn dặn giữ gìn đoàn kết như con ngươi của mắt mình nằm trong Di chúc.')
add('study-golden-book','t4-mcq-44','C','Câu Học để làm việc, làm người, làm cán bộ được ghi ở sổ vàng Trường Nguyễn Ái Quốc Trung ương năm 1949.','school')
add('arrogance-cup','t4-mcq-45','D','Đoạn trích trực tiếp phê phán tự kiêu, tự mãn. Các liên hệ giáo dục độ lượng rộng hơn không thay cho ý trực tiếp đang được hỏi.','selfcriticism',question='Đoạn so sánh người tự kiêu, tự mãn với cái chén nhỏ, đĩa cạn trực tiếp phê bình khuyết điểm nào?',note='Thêm tiêu chí ý trực tiếp để phân biệt với các cách liên hệ rộng hơn trong đáp án tổng hợp.')
add('front-form','t4-mcq-46','B','Mặt trận dân tộc thống nhất là hình thức tổ chức của khối đại đoàn kết dân tộc.','unity')
add('international-slogan','t4-mcq-47','D','Khẩu hiệu được dùng để tập hợp nhân dân yêu chuộng hòa bình và công lý, phân biệt với khẩu hiệu của Mác và Lênin.','solidarity')
add('four-colours-poem','t4-mcq-48','B','Cụm đúng là Vàng đen trắng đỏ, nhấn mạnh tình đoàn kết giữa nhân dân các dân tộc.')
add('party-and-front','t4-mcq-49','C','Đảng vừa là thành viên, vừa là lực lượng lãnh đạo Mặt trận; một mặt riêng lẻ chưa đủ.','unity')
add('self-reliance-aid','t4-mcq-50','C','Tự lực cánh sinh, dựa vào sức mình là chính tạo cơ sở để tranh thủ ngoại lực; không lấy ngoại lực làm chỗ dựa chính.')
add('duong-lectures','t5-mcq-05','D','Đường Kách mệnh tập hợp các bài giảng tại lớp huấn luyện ở Quảng Châu. Bỏ cách gọi văn kiện đầu tiên của Đảng vì tác phẩm xuất bản trước khi Đảng ra đời.','biography',question='Tác phẩm nào tập hợp các bài giảng của Nguyễn Ái Quốc tại lớp huấn luyện cán bộ ở Quảng Châu những năm 1925–1927?',note='Làm rõ câu dẫn gốc có cách gọi không chính xác về văn kiện đầu tiên của Đảng.')
add('independent-thinking','t5-mcq-08','B','Tư duy độc lập, sáng tạo cùng sự học tập, trải nghiệm giúp Hồ Chí Minh tiếp nhận có chọn lọc các giá trị văn hóa.','s2p23 s2p27')
add('father-degree','t5-mcq-10','B','Học vị đạt được trong khoa thi năm 1901 là Phó bảng, khác Tú tài, Cử nhân hoặc Tiến sĩ.','biography')
add('party-leadership-condition','t5-mcq-13','C','Sự lãnh đạo của Đảng Cộng sản là điều kiện lãnh đạo cách mạng; cần phân biệt với điều kiện lực lượng, quốc tế hoặc phương pháp.','s2p34')
add('first-complete-definition-ambiguous','t5-mcq-14','?','Câu gốc ghép ba tiêu chí không đồng nhất: lần đầu khẳng định tư tưởng ở Đại hội VII, phát triển khái niệm ở Đại hội IX, định nghĩa đầy đủ ở Đại hội XI. Cần xác định tiêu chí hoặc đáp án chính thức.',note='Chưa chấm tự động vì cách dùng lần đầu, hoàn chỉnh và Điều lệ trong cùng câu gây lẫn mốc.')
add('essay-subjective','t5-mcq-16','E','Gợi ý: phân tích phẩm chất cá nhân; tư duy độc lập, sáng tạo; hoài bão, lý tưởng; kiên cường; nhân ái; tài năng hoạt động và tổng kết thực tiễn. Khi chọn phẩm chất quan trọng, nêu tiêu chí và dẫn chứng, giải thích quan hệ với các phẩm chất khác; không có một lựa chọn A/B/C/D duy nhất.','s2p23 s2p27')
add('essay-proletarian-path','t5-mcq-17','E','Gợi ý: nêu khủng hoảng con đường cứu nước cũ; quá trình khảo nghiệm các cuộc cách mạng; tác động Cách mạng Tháng Mười và Luận cương Lênin; lựa chọn cách mạng vô sản, gắn độc lập dân tộc với tiến bộ xã hội. Phân tích ý nghĩa đối với đường lối và tổ chức lãnh đạo, tránh chỉ liệt kê mốc.','s2p2 s2p31 s2p34')
add('declaration-commitment-work','t2-g1-01 t3-mcq-21 t6-mcq-06','A','Đoạn tuyên bố quyết tâm giữ độc lập được trích từ Tuyên ngôn Độc lập năm 1945, không phải Di chúc hay lời kêu gọi kháng chiến.')
