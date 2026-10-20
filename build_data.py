from pathlib import Path
import json
import random
import re
from exam_questions import EXAM_FORMS
from exam_sets import MORE_EXAM_IDS

ROOT = Path(__file__).parent
DOC_URL = "https://docs.google.com/document/d/1iKcT1_tLk5xTTdsBzRmLEv-KpymeBbIbQSkn5-98F-A/edit"
doc_lines = (ROOT / "sources" / "ghi-chu-google-docs.txt").read_text(encoding="utf-8-sig").splitlines()
slides = json.loads((ROOT / "sources" / "slides.json").read_text(encoding="utf-8"))
slide_lookup = {(int(re.search(r"\d+", s["file"]).group()), s["slide"]): s for s in slides}

# chapter | question | answer | distractor 1 | distractor 2 | distractor 3 | source line/page
DOC = """
1|Theo ghi chú, Việt Nam đang ở giai đoạn nào?|Thời kỳ quá độ lên chủ nghĩa xã hội|Giai đoạn cao của chủ nghĩa cộng sản|Chế độ tư bản chủ nghĩa phát triển|Giai đoạn sau chủ nghĩa cộng sản|4
1|Tác phẩm đánh dấu sự ra đời của chủ nghĩa xã hội khoa học là gì?|Tuyên ngôn của Đảng Cộng sản|Phê phán Cương lĩnh Gôta|Tư bản|Chống Đuyrinh|5
1|Tuyên ngôn của Đảng Cộng sản ra đời vào năm nào?|1848|1871|1917|1895|5
1|Bộ ba phát kiến khoa học tự nhiên làm tiền đề cho chủ nghĩa xã hội khoa học gồm những gì?|Thuyết tế bào, thuyết tiến hóa và định luật bảo toàn năng lượng|Thuyết tế bào, học thuyết giá trị thặng dư và phép biện chứng|Thuyết tiến hóa, triết học cổ điển Đức và kinh tế chính trị Anh|Định luật bảo toàn năng lượng, học thuyết hình thái kinh tế và chủ nghĩa xã hội không tưởng|6
1|Nội dung nào KHÔNG thuộc ba tiền đề lý luận được ghi chú nêu?|Thuyết tế bào|Triết học cổ điển Đức|Kinh tế chính trị học cổ điển Anh|Chủ nghĩa xã hội không tưởng phê phán|7
1|Một phát hiện cơ bản của chủ nghĩa xã hội khoa học về lực lượng thay thế chủ nghĩa tư bản là gì?|Giai cấp công nhân có thể xóa bỏ chủ nghĩa tư bản và xây dựng chủ nghĩa xã hội|Giai cấp tư sản tự xóa bỏ chế độ tư bản để xây dựng chủ nghĩa xã hội|Giai cấp nông dân một mình xây dựng chủ nghĩa cộng sản|Nhà nước phong kiến là lực lượng xây dựng chủ nghĩa xã hội|8
2|Giai cấp công nhân hình thành và phát triển gắn với nền sản xuất nào?|Nền công nghiệp hiện đại|Nền thủ công nghiệp phường hội|Nền nông nghiệp tự cấp tự túc|Nền thương mại thuộc địa|13
2|Trong quan hệ sản xuất tư bản chủ nghĩa, giai cấp công nhân có đặc điểm nào?|Không sở hữu tư liệu sản xuất và bị bóc lột giá trị thặng dư|Sở hữu tư liệu sản xuất chủ yếu và thuê lao động|Nắm độc quyền ruộng đất và địa tô|Sở hữu phần lớn vốn tư bản tài chính|14
2|Theo ghi chú, giai cấp công nhân là con đẻ của nền nào?|Nền công nghiệp|Nền kinh tế tiểu nông|Nền quân chủ phong kiến|Nền thương mại cổ đại|15
2|Đặc điểm nổi bật nhất trong phương thức lao động của giai cấp công nhân là gì?|Lao động bằng phương thức công nghiệp|Lao động bằng phương thức nông nghiệp|Lao động chủ yếu theo hộ gia đình|Lao động tách biệt quá trình sản xuất hiện đại|16
2|Phẩm chất nào thuộc giai cấp công nhân theo ghi chú?|Tính tổ chức, kỷ luật và tinh thần hợp tác|Tính phân tán, tự phát và độc lập tuyệt đối|Đặc quyền sở hữu tư liệu sản xuất|Không chịu sự ràng buộc của lao động xã hội|16
2|Nội dung cốt lõi của sứ mệnh lịch sử giai cấp công nhân là gì?|Xóa bỏ chủ nghĩa tư bản, xây dựng chủ nghĩa xã hội|Cải thiện chủ nghĩa tư bản mà không thay đổi chế độ|Khôi phục phương thức sản xuất phong kiến|Duy trì nguyên trạng quan hệ sản xuất tư bản|18
2|Điều kiện khách quan quy định sứ mệnh lịch sử của giai cấp công nhân là gì?|Địa vị kinh tế và địa vị chính trị - xã hội của giai cấp công nhân|Chỉ ý chí cá nhân của lãnh tụ công nhân|Chỉ số lượng đảng viên trong xã hội|Sự lựa chọn tự do của giai cấp tư sản|19
2|Nhân tố chủ quan quan trọng nhất để giai cấp công nhân thực hiện sứ mệnh lịch sử là gì?|Đảng Cộng sản lãnh đạo|Giai cấp tư sản lãnh đạo|Bộ máy nhà nước phong kiến|Các hiệp hội chủ doanh nghiệp|20
2|Giai cấp công nhân Việt Nam ra đời vào thời điểm nào theo ghi chú?|Đầu thế kỷ XX|Đầu thế kỷ XIX|Sau năm 1975|Cuối thế kỷ XVIII|21
2|Đảng Cộng sản được hình thành từ sự kết hợp nào theo ghi chú?|Phong trào công nhân và chủ nghĩa Mác - Lênin|Phong trào nông dân và kinh tế chính trị cổ điển Anh|Phong trào tư sản và chủ nghĩa xã hội không tưởng|Phong trào công nhân và tư tưởng phong kiến|22
2|Nội dung kinh tế của sứ mệnh lịch sử giai cấp công nhân là gì?|Sản xuất của cải cho xã hội xã hội chủ nghĩa với tư cách lực lượng sản xuất cơ bản|Chỉ tổ chức bộ máy hành chính nhà nước|Chỉ xây dựng hệ tư tưởng và văn hóa mới|Thay thế chức năng sản xuất của toàn bộ xã hội|23
2|Nội dung chính trị - xã hội của sứ mệnh lịch sử giai cấp công nhân là gì?|Đấu tranh giành chính quyền và xây dựng nhà nước mới của nhân dân|Chỉ nâng cao năng suất lao động công nghiệp|Chỉ xây dựng đạo đức xã hội chủ nghĩa|Duy trì nhà nước của giai cấp tư sản|24
2|Nội dung văn hóa, tư tưởng của sứ mệnh lịch sử giai cấp công nhân là gì?|Xây dựng văn hóa và con người mới với tư tưởng, đạo đức xã hội chủ nghĩa|Chỉ mở rộng tư hữu tư liệu sản xuất|Chỉ giành chính quyền nhà nước|Khôi phục toàn bộ hệ tư tưởng phong kiến|25
2|Điểm tương đồng của công nhân hiện nay và thế kỷ XIX là gì?|Vẫn chịu sự bóc lột giá trị thặng dư|Đã hoàn toàn không còn xung đột lợi ích với tư sản|Không còn là lực lượng sản xuất chủ yếu|Không còn tham gia đấu tranh xã hội|28
2|Xu hướng “công nhân tri thức” phản ánh biến đổi nào của giai cấp công nhân hiện đại?|Trí tuệ hóa|Phi công nghiệp hóa|Phong kiến hóa|Tách khỏi lao động xã hội|29
2|“Trung lưu hóa” công nhân được ghi chú gắn với quá trình nào?|Công nhân tham gia vào sở hữu|Công nhân mất hoàn toàn mọi kỹ năng|Công nhân rời bỏ nền công nghiệp|Công nhân nắm độc quyền nhà nước|29
2|Ở các nước định hướng xã hội chủ nghĩa, nội dung chính trị của sứ mệnh công nhân hiện nay là gì?|Lãnh đạo nhân dân xây dựng chủ nghĩa xã hội|Giữ nguyên quyền lực của tư sản|Chỉ tranh đấu để tăng tiền lương|Không tham gia xây dựng nhà nước|32
2|Ở các nước tư bản, vai trò chính trị của công nhân hiện nay được ghi chú là gì?|Đi đầu đấu tranh chống áp bức và bất công|Trở thành tầng lớp thống trị nhà nước tư sản|Ngừng mọi hoạt động đấu tranh xã hội|Chỉ tham gia xây dựng văn hóa mới|33
2|Về văn hóa - xã hội, công nhân hiện nay góp phần xây dựng nền văn hóa hướng tới điều gì?|Công bằng, bình đẳng và quyền con người|Đặc quyền của một tầng lớp sở hữu|Xóa bỏ mọi tổ chức văn hóa|Phân chia quyền lợi theo nguồn gốc giai cấp|34
3|Chủ nghĩa xã hội là giai đoạn nào của hình thái kinh tế - xã hội cộng sản chủ nghĩa?|Giai đoạn đầu|Giai đoạn cao|Giai đoạn trước chủ nghĩa tư bản|Giai đoạn nằm ngoài hình thái cộng sản|37
3|Mâu thuẫn kinh tế dẫn tới sự ra đời của chủ nghĩa xã hội theo ghi chú là gì?|Giữa lực lượng sản xuất và quan hệ sản xuất trong chủ nghĩa tư bản|Giữa hai hệ tư tưởng trong xã hội phong kiến|Giữa các nhóm văn hóa trong cộng đồng|Giữa nông nghiệp và thương nghiệp cổ đại|39
3|Mâu thuẫn chính trị - xã hội trong chủ nghĩa tư bản được ghi chú là gì?|Giữa giai cấp công nhân và giai cấp tư sản|Giữa các nhóm công nhân với nhau|Giữa chủ nô và nô lệ thời cổ đại|Giữa địa chủ và nông dân phong kiến|40
3|Đặc trưng kinh tế bản chất của chủ nghĩa xã hội theo ghi chú là gì?|Kinh tế phát triển cao dựa trên lực lượng sản xuất hiện đại và công hữu tư liệu sản xuất chủ yếu|Kinh tế dựa trên lực lượng sản xuất lạc hậu và tư hữu tuyệt đối|Kinh tế không cần tư liệu sản xuất và quan hệ sở hữu|Kinh tế phát triển cao nhưng không có lực lượng sản xuất hiện đại|42
3|Nhà nước xã hội chủ nghĩa đầu tiên trong thực tiễn xuất hiện sau sự kiện nào?|Cách mạng Tháng Mười Nga năm 1917|Công xã Pari năm 1871|Tuyên ngôn Đảng Cộng sản năm 1848|Đại hội IX của Đảng năm 2001|43
3|Theo ghi chú, con đường thực hiện cách mạng vô sản là gì?|Bạo lực cách mạng|Thỏa hiệp hoàn toàn với giai cấp tư sản|Chỉ cải cách kinh tế tự phát|Chỉ thay đổi trong lĩnh vực văn hóa|44
3|Thời kỳ quá độ lên chủ nghĩa xã hội có tính chất nào?|Tất yếu đối với các nước xây dựng chủ nghĩa xã hội|Chỉ xảy ra ở các nước tư bản phát triển|Chỉ xảy ra ở Việt Nam|Có thể bỏ qua ở mọi quốc gia|46
3|Lênin dùng hình ảnh nào để nói về khó khăn của thời kỳ quá độ?|Những cơn đau đẻ kéo dài|Một bước nhảy tức thời|Một thời kỳ không có mâu thuẫn|Một quá trình tự động hoàn tất|47
3|Quá độ trực tiếp được ghi chú mô tả từ đâu?|Từ chủ nghĩa tư bản ở nước tư bản phát triển lên chủ nghĩa cộng sản|Từ xã hội tiền tư bản lên chủ nghĩa tư bản|Từ xã hội phong kiến lên nhà nước chủ nô|Từ chủ nghĩa xã hội về xã hội phong kiến|50
3|Việt Nam được ghi chú là ví dụ của kiểu quá độ nào?|Quá độ gián tiếp|Quá độ trực tiếp ở nước tư bản phát triển|Quá độ từ giai đoạn cao về giai đoạn thấp|Quá độ không qua bất kỳ giai đoạn nào|51
3|Điểm nổi bật của thời kỳ quá độ là gì?|Các yếu tố xã hội cũ và mới đan xen trên mọi lĩnh vực|Chỉ còn các yếu tố của xã hội mới|Không có biến đổi trong lĩnh vực kinh tế|Mọi lĩnh vực phát triển đồng nhất ngay lập tức|54
3|Đặc điểm kinh tế của thời kỳ quá độ là gì?|Nhiều thành phần kinh tế vận động theo định hướng xã hội chủ nghĩa|Chỉ tồn tại một thành phần kinh tế duy nhất|Không có quan hệ sản xuất nào|Mọi thành phần kinh tế đều tách khỏi định hướng xã hội|54
3|“Bỏ qua chế độ tư bản chủ nghĩa” ở Việt Nam có nghĩa chính xác là gì?|Bỏ qua việc xác lập vị trí thống trị của quan hệ sản xuất và kiến trúc thượng tầng tư bản chủ nghĩa|Bỏ qua tất cả thành tựu khoa học và công nghệ của nhân loại|Bỏ qua quá trình phát triển lực lượng sản xuất|Bỏ qua toàn bộ quan hệ kinh tế trong thời kỳ quá độ|57
3|Theo C. Mác, xã hội thời kỳ quá độ còn mang điều gì?|Những dấu vết của xã hội cũ|Đầy đủ đặc điểm của giai đoạn cộng sản cao|Không có bất cứ yếu tố nào từ quá khứ|Chỉ dấu vết của xã hội tương lai|58
3|Có bao nhiêu đặc trưng của chủ nghĩa xã hội ở Việt Nam được tài liệu liệt kê?|Tám|Ba|Bốn|Sáu|60
3|Đặc trưng về chủ thể quyền lực của chủ nghĩa xã hội ở Việt Nam là gì?|Do nhân dân làm chủ|Do một nhóm tư hữu làm chủ|Do nhà nước phong kiến làm chủ|Do doanh nghiệp nước ngoài làm chủ|60
3|Đặc trưng văn hóa của chủ nghĩa xã hội Việt Nam được nêu thế nào?|Tiên tiến, đậm đà bản sắc dân tộc|Chỉ tiếp nhận văn hóa ngoại nhập|Tách khỏi mọi giá trị dân tộc|Chỉ bảo tồn văn hóa mà không phát triển|60
3|Đặc trưng về các dân tộc trong chủ nghĩa xã hội Việt Nam là gì?|Bình đẳng, đoàn kết, tôn trọng và giúp nhau cùng phát triển|Cạnh tranh để xác lập một dân tộc có đặc quyền|Tách biệt tuyệt đối và không hợp tác|Chỉ bình đẳng về hình thức, không cần đoàn kết|60
3|Đặc trưng đối ngoại của chủ nghĩa xã hội Việt Nam là gì?|Quan hệ hữu nghị, hợp tác với các nước trên thế giới|Không có quan hệ với bất kỳ quốc gia nào|Chỉ quan hệ với một nước duy nhất|Tách biệt khỏi hợp tác quốc tế|60
3|Có bao nhiêu phương hướng xây dựng chủ nghĩa xã hội ở Việt Nam được tài liệu nêu?|Tám|Ba|Bốn|Mười|61
3|Phương hướng kinh tế quan trọng được nêu là gì?|Phát triển kinh tế thị trường định hướng xã hội chủ nghĩa|Xóa bỏ mọi quan hệ thị trường ngay lập tức|Quay lại nền kinh tế tự cung tự cấp|Duy trì mô hình kinh tế tư bản chủ nghĩa thuần túy|61
3|Phương hướng về quốc phòng và an ninh là gì?|Bảo đảm quốc phòng, an ninh và trật tự, an toàn xã hội|Chỉ tập trung kinh tế, bỏ quốc phòng|Chỉ tập trung quốc phòng, bỏ trật tự xã hội|Chuyển toàn bộ nhiệm vụ an ninh ra nước ngoài|61
3|Trong bốn trụ cột phát triển, nhiệm vụ nào là trung tâm?|Phát triển kinh tế - xã hội|Xây dựng Đảng|Phát triển văn hóa, con người|Củng cố quốc phòng, an ninh|62
3|Trong bốn trụ cột phát triển, nhiệm vụ nào là then chốt?|Xây dựng Đảng|Phát triển kinh tế - xã hội|Phát triển văn hóa, con người|Củng cố quốc phòng, an ninh|62
3|Trong bốn trụ cột phát triển, nền tảng tinh thần là gì?|Phát triển văn hóa, con người|Xây dựng Đảng|Phát triển kinh tế - xã hội|Củng cố quốc phòng, an ninh|62
3|Nhiệm vụ trọng yếu, thường xuyên trong bốn trụ cột là gì?|Củng cố quốc phòng, an ninh|Xây dựng Đảng|Phát triển kinh tế - xã hội|Phát triển văn hóa, con người|62
3|Nội dung nào thuộc ba khâu đột phá được ghi chú?|Phát triển nguồn nhân lực chất lượng cao|Bỏ qua phát triển kết cấu hạ tầng|Xóa bỏ mọi thể chế kinh tế thị trường|Thay thế toàn bộ lao động bằng nhập khẩu|63
4|Nghĩa gốc của dân chủ là gì?|Quyền lực thuộc về nhân dân|Quyền lực thuộc về nhà vua|Quyền lực thuộc về chủ nô|Quyền lực thuộc về tư bản|67
4|“Demos” trong thuật ngữ dân chủ có nghĩa là gì?|Nhân dân|Quyền lực|Nhà nước|Pháp luật|68
4|“Kratos” trong thuật ngữ dân chủ có nghĩa là gì?|Quyền lực|Nhân dân|Nhà nước|Pháp luật|68
4|Theo ghi chú, thuật ngữ dân chủ ra đời vào thời gian nào?|Thế kỷ VII–VI trước Công nguyên|Thế kỷ VII–VI sau Công nguyên|Thế kỷ XVIII sau Công nguyên|Thế kỷ XX sau Công nguyên|69
4|Theo Ăngghen, kiểu dân chủ nào tồn tại ở hình thái nguyên thủy?|Dân chủ quân sự|Dân chủ tư sản|Dân chủ xã hội chủ nghĩa|Dân chủ chủ nô|70
4|Trên phương diện tổ chức và quản lý xã hội, dân chủ là gì?|Một nguyên tắc|Một lực lượng sản xuất|Một kiểu sở hữu tư liệu sản xuất|Một hình thức phân phối|71
4|Trên phương diện quyền lực, dân chủ được hiểu thế nào?|Quyền lực thuộc về nhân dân|Quyền lực thuộc về riêng chính đảng|Quyền lực thuộc về chủ sở hữu tư bản|Quyền lực thuộc về nhà nước phong kiến|72
4|Trên phương diện chế độ xã hội và chính trị, dân chủ là gì?|Một hình thức nhà nước|Một hình thức lao động|Một quan hệ sản xuất|Một phương pháp phân phối|73
4|Theo Lênin, dân chủ là sự thống trị của ai?|Đa số|Thiểu số|Một cá nhân|Một dòng họ|75
4|Hồ Chí Minh diễn đạt dân chủ thế nào?|Dân là chủ, dân làm chủ|Nhà nước là chủ, dân tuân thủ|Giai cấp tư sản là chủ|Dân chỉ là đối tượng quản lý|76
4|Trong xã hội cộng sản nguyên thủy, nền dân chủ được sơ đồ ghi chú xác định thế nào?|Chưa có nền dân chủ|Có dân chủ tư sản|Có dân chủ vô sản|Có dân chủ chủ nô|78
4|Nền dân chủ tương ứng với xã hội chiếm hữu nô lệ là gì?|Dân chủ chủ nô|Dân chủ tư sản|Dân chủ xã hội chủ nghĩa|Quân chủ phong kiến|78
4|Nền dân chủ tương ứng với xã hội tư bản là gì?|Dân chủ tư sản|Dân chủ chủ nô|Dân chủ xã hội chủ nghĩa|Quân chủ phong kiến|78
4|Theo Lênin, sau dân chủ tư sản là hình thức nào trong tiến trình phát triển dân chủ?|Dân chủ vô sản|Dân chủ chủ nô|Chuyên chế phong kiến|Không còn dân chủ ngay lập tức|79
4|Dân chủ xã hội chủ nghĩa ra đời sau thắng lợi nào?|Cách mạng Tháng Mười Nga năm 1917|Công xã Pari năm 1871|Tuyên ngôn năm 1848|Cách mạng công nghiệp ở Anh|81
4|Bản chất chính trị của dân chủ xã hội chủ nghĩa gắn với giai cấp nào?|Giai cấp công nhân|Giai cấp tư sản|Giai cấp chủ nô|Giai cấp địa chủ phong kiến|82
4|Bản chất kinh tế của dân chủ xã hội chủ nghĩa dựa trên gì?|Sở hữu xã hội đối với tư liệu sản xuất chủ yếu|Sở hữu tư nhân tuyệt đối đối với mọi tư liệu sản xuất|Sở hữu chủ nô đối với người lao động|Sở hữu phong kiến đối với ruộng đất|82
4|Hệ tư tưởng chủ đạo thuộc bản chất tư tưởng của dân chủ xã hội chủ nghĩa là gì?|Chủ nghĩa Mác - Lênin|Chủ nghĩa tự do tư sản|Tư tưởng phong kiến|Chủ nghĩa xã hội không tưởng tiền Mác|82
4|Ở Việt Nam, dân chủ có vai trò nào đối với chế độ xã hội chủ nghĩa?|Mục tiêu, bản chất và động lực|Chỉ là mục tiêu, không là động lực|Chỉ là công cụ kinh tế|Chỉ là nguyên tắc đối ngoại|84
4|Ba cách gọi nhà nước xã hội chủ nghĩa trong ghi chú là gì?|Nhà nước kiểu mới, nửa nhà nước, không còn nguyên nghĩa|Nhà nước chủ nô, phong kiến, tư sản|Nhà nước đối nội, đối ngoại, kinh tế|Nhà nước trung ương, địa phương, khu vực|87
4|Mục đích cuối cùng của nhà nước xã hội chủ nghĩa là gì?|Cải tạo xã hội cũ và xây dựng thành công xã hội mới|Duy trì nguyên vẹn nhà nước tư sản|Chỉ quản lý hoạt động sản xuất|Chỉ tổ chức lĩnh vực văn hóa|88
4|Trong nhà nước xã hội chủ nghĩa, chủ thể quyền lực nhà nước là ai?|Nhân dân|Giai cấp tư sản|Chủ nô|Địa chủ phong kiến|90
4|Nhà nước pháp quyền xã hội chủ nghĩa Việt Nam tổ chức và hoạt động trên cơ sở nào?|Hiến pháp và pháp luật|Ý chí tùy nghi của từng cơ quan|Tập quán địa phương thay cho pháp luật|Quyết định riêng của doanh nghiệp|94
4|Quyền lực nhà nước ở Việt Nam được ghi chú mô tả thế nào?|Thống nhất, có phân công, phối hợp và kiểm soát giữa lập pháp, hành pháp, tư pháp|Tách rời hoàn toàn và không có kiểm soát giữa các quyền|Chỉ tập trung vào cơ quan hành pháp|Giao hoàn toàn cho tổ chức kinh tế|94
4|Nguyên tắc tổ chức bộ máy nhà nước pháp quyền xã hội chủ nghĩa Việt Nam là gì?|Tập trung dân chủ|Tự phát phi tập trung|Phân quyền tuyệt đối không phối hợp|Quân chủ tập quyền|94
3|Có mấy kiểu quá độ lên chủ nghĩa xã hội được ghi chú phân biệt?|Hai kiểu: trực tiếp và gián tiếp|Một kiểu: chỉ trực tiếp|Ba kiểu: trực tiếp, gián tiếp và trung gian|Bốn kiểu theo bốn lĩnh vực xã hội|49
3|So với Mác - Ăngghen, sơ đồ của Lênin tách rõ giai đoạn nào?|Thời kỳ quá độ lên chủ nghĩa xã hội, chủ nghĩa xã hội và giai đoạn cao của chủ nghĩa cộng sản|Chỉ chủ nghĩa tư bản và xã hội phong kiến|Chỉ giai đoạn thấp và giai đoạn cao, không có thời kỳ quá độ|Chỉ kinh tế thị trường và nhà nước pháp quyền|52
3|Ghi chú bên lề slide nêu chủ thể nắm quyền lực nhà nước trong thời kỳ quá độ là ai?|Giai cấp công nhân|Giai cấp tư sản|Giai cấp địa chủ|Giai cấp chủ nô|55
3|Mục tiêu tổng quát trong tám đặc trưng của chủ nghĩa xã hội Việt Nam là gì?|Dân giàu, nước mạnh, dân chủ, công bằng, văn minh|Chỉ tăng trưởng kinh tế, không cần công bằng|Chỉ xây dựng văn hóa, không cần dân chủ|Chỉ phát triển quốc phòng, không cần văn minh|60
3|Đặc trưng về con người trong chủ nghĩa xã hội Việt Nam là gì?|Ấm no, tự do, hạnh phúc và có điều kiện phát triển toàn diện|Chỉ có quyền lao động, không có quyền phát triển|Chỉ có đời sống vật chất, không có tự do|Chỉ có hạnh phúc cá nhân, không có quyền xã hội|60
3|Đặc trưng của Nhà nước pháp quyền xã hội chủ nghĩa Việt Nam trong tám đặc trưng là gì?|Của nhân dân, do nhân dân, vì nhân dân, do Đảng Cộng sản lãnh đạo|Của một tầng lớp sở hữu, do tư bản lãnh đạo|Không cần pháp luật và không có chủ thể nhân dân|Chỉ của bộ máy hành chính, không do nhân dân|60
3|Phương hướng công nghiệp hóa, hiện đại hóa gắn với yếu tố nào?|Kinh tế tri thức và bảo vệ tài nguyên, môi trường|Chỉ mở rộng khai thác tài nguyên vô hạn|Tách khỏi khoa học và công nghệ|Loại bỏ mục tiêu bảo vệ môi trường|61
3|Phương hướng xây dựng xã hội trên lĩnh vực văn hóa và con người nhấn mạnh điều gì?|Nâng cao đời sống và thực hiện tiến bộ, công bằng xã hội|Chỉ tăng sản lượng công nghiệp|Tách văn hóa khỏi phát triển con người|Chỉ bảo tồn tập quán, không cần công bằng|61
3|Phương hướng xây dựng hệ thống chính trị ở Việt Nam bao gồm gì?|Xây dựng dân chủ xã hội chủ nghĩa và đại đoàn kết toàn dân tộc|Bãi bỏ mọi hình thức dân chủ và đoàn kết|Chỉ thay đổi bộ máy kinh tế|Tách nhân dân khỏi đời sống chính trị|61
3|Phương hướng về Nhà nước trong thời kỳ quá độ ở Việt Nam là gì?|Xây dựng Nhà nước pháp quyền xã hội chủ nghĩa của nhân dân, do nhân dân, vì nhân dân|Xây dựng nhà nước của riêng giới sở hữu tư bản|Giảm vai trò của Hiến pháp và pháp luật|Đặt nhân dân ngoài chủ thể quyền lực|61
3|Phương hướng cuối trong tám phương hướng xây dựng chủ nghĩa xã hội là gì?|Xây dựng Đảng trong sạch, vững mạnh|Giải thể mọi tổ chức chính trị|Duy trì bộ máy nhà nước phong kiến|Ngừng xây dựng lực lượng lãnh đạo|61
4|Theo Mác - Lênin, dân chủ là một hình thức tổ chức nhà nước của ai?|Giai cấp thống trị|Chỉ cộng đồng nguyên thủy|Chỉ các tổ chức kinh tế|Chỉ một nhóm trí thức|74
4|Nội dung nào thuộc các cách nhìn về dân chủ được ghi chú liệt kê?|Giá trị xã hội và nguyên tắc hoạt động của tổ chức chính trị - xã hội|Chỉ là một phương pháp sản xuất công nghiệp|Chỉ là một chế độ sở hữu ruộng đất|Chỉ là một công cụ kỹ thuật hành chính|77
4|Đặc điểm nào được tài liệu dùng để mô tả dân chủ xã hội chủ nghĩa cao hơn về chất?|Quyền lực thuộc về nhân dân, dân chủ gắn với pháp luật|Quyền lực thuộc về một nhóm tư hữu, tách khỏi pháp luật|Quyền lực thuộc về nhà nước chủ nô|Không cần người dân thực hiện quyền làm chủ|83
4|Quan niệm chung về nhà nước pháp quyền yêu cầu các cơ quan nhà nước như thế nào?|Kiểm soát lẫn nhau và phục vụ nhân dân|Không chịu kiểm soát lẫn nhau|Hoạt động chỉ vì lợi ích cơ quan|Không cần tuân thủ pháp luật|93
"""

SLIDE = """
1|Trong ba bộ phận của chủ nghĩa Mác - Lênin, chủ nghĩa xã hội khoa học nghiên cứu trọng tâm gì?|Những quy luật chính trị - xã hội của hình thái kinh tế - xã hội cộng sản chủ nghĩa|Những quy luật chung nhất của tự nhiên, xã hội và tư duy|Chỉ những quy luật giá trị trong nền kinh tế tư bản|Chỉ các kỹ thuật quản lý doanh nghiệp công nghiệp|4:1
1|Theo slide, cách mạng công nghiệp đầu thế kỷ XIX làm xuất hiện lực lượng sản xuất nào?|Nền đại công nghiệp|Nền thủ công nghiệp trung cổ|Nền nông nghiệp tự cấp|Nền thương nghiệp nô lệ|9:1
1|Nguyên nhân phong trào công nhân ban đầu thất bại theo slide là gì?|Thiếu lý luận khoa học, cách mạng|Thiếu mâu thuẫn với giai cấp tư sản|Không xuất hiện nền công nghiệp hiện đại|Đã có chính quyền công nhân ổn định|10:1
1|Ba phát hiện vĩ đại của Mác và Ăngghen gồm những gì?|Duy vật lịch sử, giá trị thặng dư, sứ mệnh lịch sử của giai cấp công nhân|Tế bào, tiến hóa, bảo toàn năng lượng|Triết học Đức, kinh tế chính trị Anh, xã hội chủ nghĩa không tưởng|Đấu tranh giai cấp, thị trường tự do, quân chủ lập hiến|15:1
1|Điểm chuyển biến lập trường triết học của Mác và Ăngghen là gì?|Từ duy tâm sang duy vật|Từ duy vật sang duy tâm|Từ biện chứng sang siêu hình|Từ xã hội chủ nghĩa sang phong kiến|14:1
1|Tuyên ngôn của Đảng Cộng sản được slide xác định là gì?|Cương lĩnh chính trị đầu tiên của phong trào công nhân và các đảng Cộng sản|Bản tuyên ngôn của nhà nước tư sản đầu tiên|Một báo cáo về công xã Pari năm 1871|Một giáo trình về nhà nước pháp quyền Việt Nam|18:1
1|Tư tưởng cách mạng không ngừng nhấn mạnh điều gì?|Các giai đoạn cách mạng nối tiếp nhau, không có giai đoạn ngừng nghỉ|Mỗi giai đoạn tách biệt hoàn toàn, không làm tiền đề cho nhau|Chỉ có một giai đoạn duy nhất trong mọi cuộc cách mạng|Cách mạng tự động thắng lợi mà không cần nhiệm vụ cụ thể|21:1
1|Theo slide, mục tiêu đầu tiên của giai cấp vô sản là gì?|Giành chính quyền|Hoàn thành ngay xã hội cộng sản giai đoạn cao|Xây dựng quan hệ sở hữu chủ nô|Bãi bỏ mọi hình thức tổ chức chính trị|22:1
1|Trong liên minh công nhân - nông dân, vai trò lãnh đạo thuộc về ai?|Giai cấp công nhân|Giai cấp nông dân|Giai cấp tư sản|Tầng lớp địa chủ|23:1
1|Theo slide, chính đảng cách mạng của giai cấp vô sản có nhiệm vụ gì?|Đoàn kết công nhân, tập hợp người lao động và truyền bá lý luận khoa học|Chỉ tổ chức sản xuất trong doanh nghiệp|Tách công nhân khỏi các tầng lớp lao động|Chỉ duy trì cuộc đấu tranh kinh tế tự phát|24:1
1|Sau Công xã Pari, tư tưởng nhà nước kiểu mới nêu quyền gì với đại diện được bầu?|Có thể bãi miễn nếu không xứng đáng|Được giữ chức suốt đời|Có đặc quyền không thể kiểm soát|Không phải chịu trách nhiệm trước nhân dân|26:1
1|Công cụ cải biến xã hội trong thời kỳ quá độ theo slide là gì?|Nhà nước chuyên chính của giai cấp vô sản|Bộ máy nhà nước của giai cấp bóc lột|Các tập đoàn tư bản độc quyền|Chỉ hoạt động kinh tế tự phát|28:1
1|Công lao lớn nhất của Lênin theo slide là gì?|Làm cho lý luận chủ nghĩa xã hội khoa học trở thành hiện thực|Viết Tuyên ngôn của Đảng Cộng sản|Phát hiện học thuyết giá trị thặng dư|Sáng lập Công xã Pari năm 1871|31:1
1|Phương pháp nào thuộc phương pháp nghiên cứu chủ nghĩa xã hội khoa học?|Kết hợp lịch sử và lôgíc|Chỉ suy diễn không cần thực tiễn|Chỉ khảo sát hiện tượng tự nhiên|Loại bỏ phân tích chính trị - xã hội|35:1
1|Đối tượng nghiên cứu của chủ nghĩa xã hội khoa học tập trung vào quá trình nào?|Sự hình thành và phát triển hình thái kinh tế - xã hội cộng sản chủ nghĩa|Chỉ quá trình trao đổi hàng hóa trong xã hội cổ đại|Chỉ sự hình thành các loài sinh vật|Chỉ kỹ thuật vận hành máy móc công nghiệp|34:1
2|Giai cấp công nhân được slide định nghĩa gắn với quá trình nào?|Hình thành và phát triển của công nghiệp hiện đại|Hình thành chế độ chiếm hữu nô lệ|Phát triển độc quyền ruộng đất phong kiến|Chuyển từ sản xuất công nghiệp về thủ công nghiệp|4:2
2|Công cụ lao động đặc trưng của phương thức công nghiệp theo slide là gì?|Máy móc|Chỉ công cụ đá nguyên thủy|Chỉ sức kéo súc vật|Chỉ ruộng đất phong kiến|5:2
2|Sứ mệnh lịch sử của công nhân được thực hiện thông qua đội tiên phong nào?|Đảng Cộng sản|Giai cấp tư sản|Bộ máy nhà nước phong kiến|Tổ chức chủ nô|6:2
2|Sứ mệnh lịch sử của công nhân hướng tới lợi ích của ai?|Giai cấp công nhân và đông đảo nhân dân lao động|Chỉ một nhóm tư bản độc quyền|Chỉ bộ máy quan liêu|Chỉ các chủ sở hữu tư liệu sản xuất|8:2
2|Mục tiêu về sở hữu trong sứ mệnh công nhân là gì?|Xóa bỏ chế độ tư hữu tư bản chủ nghĩa về tư liệu sản xuất chủ yếu|Thay một chế độ sở hữu tư nhân bằng chế độ sở hữu tư nhân khác|Khôi phục sở hữu của chủ nô|Giữ nguyên chế độ tư hữu tư bản chủ nghĩa|8:2
2|Điều kiện nào giúp một giai cấp đảm nhiệm sứ mệnh lịch sử theo slide?|Đại diện cho phương thức sản xuất tiên tiến|Không có hệ tư tưởng riêng|Lợi ích trái với đa số xã hội|Không cần tổ chức chính đảng|9:2
2|Điều kiện chủ quan của giai cấp công nhân gồm yếu tố nào?|Sự phát triển về số lượng và chất lượng của bản thân giai cấp|Chỉ sự suy yếu của lực lượng sản xuất|Chỉ mâu thuẫn trong quan hệ sản xuất tư bản|Chỉ sự tăng trưởng của giai cấp tư sản|11:2
2|Cơ sở xã hội quan trọng nhất của Đảng Cộng sản theo slide là gì?|Giai cấp công nhân|Giai cấp tư sản|Giai cấp địa chủ|Tầng lớp chủ nô|12:2
2|Vai trò “tham mưu giai cấp” của Đảng Cộng sản thể hiện ở việc nào?|Vạch cương lĩnh, đường lối đấu tranh chính trị|Chỉ tổ chức sản xuất vật chất|Chỉ giữ các chức năng đối ngoại|Không tạo sự thống nhất tư tưởng|13:2
2|Công nhân Việt Nam ra đời từ quá trình nào theo slide?|Khai thác thuộc địa của thực dân Pháp|Cách mạng công nghiệp ở Anh|Công xã Pari năm 1871|Sự thành lập Liên Xô|18:2
2|Một ưu thế chính trị của giai cấp công nhân Việt Nam là gì?|Sớm tiếp thu chủ nghĩa Mác - Lênin|Sớm sở hữu phần lớn tư liệu sản xuất|Không liên hệ với phong trào dân tộc|Không chịu ảnh hưởng của chiến tranh|19:2
2|Giai cấp công nhân Việt Nam có quan hệ đặc biệt mật thiết với giai cấp nào?|Giai cấp nông dân|Giai cấp chủ nô|Giai cấp địa chủ|Giai cấp tư sản độc quyền|20:2
2|Phương hướng xây dựng công nhân Việt Nam hiện nay theo slide là gì?|Tăng cường trí thức hóa công nhân|Giảm chất lượng nguồn nhân lực|Tách công đoàn khỏi người lao động|Ngừng công nghiệp hóa, hiện đại hóa|22:2
3|Theo slide, chủ nghĩa xã hội thuộc giai đoạn nào của hình thái cộng sản chủ nghĩa?|Giai đoạn thấp|Giai đoạn cao|Giai đoạn trước chủ nghĩa tư bản|Giai đoạn ngoài hình thái cộng sản|5:3
3|Đặc trưng phân phối trong chủ nghĩa xã hội theo slide là gì?|Phân phối theo lao động|Phân phối theo đặc quyền dòng họ|Phân phối theo chế độ nô lệ|Không có nguyên tắc phân phối|8:3
3|Mục tiêu cao nhất của chủ nghĩa xã hội theo slide là gì?|Giải phóng và phát triển con người toàn diện|Chỉ tăng sản lượng công nghiệp|Chỉ thay đổi bộ máy hành chính|Chỉ bảo tồn quan hệ sản xuất cũ|8:3
3|Theo slide, C. Mác nhấn mạnh thực chất nào của thời kỳ quá độ?|Quá độ chính trị|Chỉ quá độ về ngôn ngữ|Chỉ quá độ về địa lý|Không có quá độ trong đời sống xã hội|11:3
3|Lênin làm rõ thêm mặt nào của thời kỳ quá độ theo slide?|Quá độ trong kinh tế|Chỉ thay đổi tên gọi nhà nước|Chỉ thay đổi biên giới quốc gia|Không cần phát triển lực lượng sản xuất|11:3
3|Trong thời kỳ quá độ, lĩnh vực tư tưởng - văn hóa có đặc điểm gì?|Tồn tại nhiều tư tưởng, văn hóa khác nhau|Chỉ tồn tại một quan điểm duy nhất ngay lập tức|Hoàn toàn không có giá trị cũ|Không có biến đổi về giá trị xã hội|12:3
3|Đặc điểm thời kỳ quá độ ở Việt Nam theo slide là gì?|Bỏ qua chế độ tư bản chủ nghĩa|Trực tiếp từ nước tư bản phát triển|Không cần thời kỳ quá độ|Bỏ qua mọi thành tựu của nhân loại|14:3
3|Khi quá độ bỏ qua chế độ tư bản, Việt Nam vẫn tiếp thu điều gì?|Thành tựu của nhân loại, đặc biệt khoa học và công nghệ|Vị trí thống trị của quan hệ sản xuất tư bản|Vị trí thống trị của kiến trúc thượng tầng tư bản|Sự đình trệ của lực lượng sản xuất|16:3
3|Một trong ba khâu đột phá của Việt Nam là gì?|Phát triển kết cấu hạ tầng đồng bộ|Loại bỏ phát triển nguồn nhân lực|Đình chỉ hoàn thiện thể chế kinh tế|Thu hẹp toàn bộ hệ thống hạ tầng|17:3
3|Đặc trưng kinh tế của xã hội xã hội chủ nghĩa ở Việt Nam theo slide là gì?|Lực lượng sản xuất hiện đại và quan hệ sản xuất tiến bộ, phù hợp|Lực lượng sản xuất lạc hậu và quan hệ sản xuất phong kiến|Chỉ phát triển thương nghiệp, không cần sản xuất|Quan hệ sản xuất tư bản thống trị hoàn toàn|18:3
3|Phương hướng về đối ngoại của Việt Nam được slide nêu là gì?|Độc lập, tự chủ, hòa bình, hữu nghị, hợp tác và hội nhập|Chỉ cô lập khỏi mọi quan hệ quốc tế|Phụ thuộc hoàn toàn vào một cường quốc|Không tham gia các hình thức hợp tác|20:3
4|Nghĩa gốc của dân chủ theo slide là gì?|Quyền lực của nhân dân|Quyền lực của quân chủ|Quyền lực của chủ nô|Quyền lực của tư bản|4:4
4|Nhà nước dân chủ tại Aten thời cổ đại thuộc kiểu nào?|Dân chủ chủ nô|Dân chủ tư sản|Dân chủ vô sản|Dân chủ xã hội chủ nghĩa|9:4
4|Theo quan niệm Mác - Lênin, dân chủ gắn với nhà nước mang bản chất của ai?|Giai cấp thống trị xã hội|Mọi giai cấp như nhau trong mọi thời kỳ|Chỉ tầng lớp trí thức|Chỉ cộng đồng nguyên thủy|17:4
4|Dân chủ xét như một phạm trù lịch sử gắn với điều gì?|Quá trình ra đời, phát triển của xã hội loài người|Một công cụ kỹ thuật không đổi|Một quan hệ sở hữu không biến đổi|Một kiểu nhà nước duy nhất|19:4
4|Trong xã hội cộng sản chủ nghĩa giai đoạn cao, nền dân chủ được slide mô tả thế nào?|Mất đi khi giai cấp và nhà nước không còn|Chuyển thành dân chủ chủ nô|Trở lại dân chủ tư sản|Được thay bằng quân chủ phong kiến|27:4
4|Theo slide, trình độ thực hiện dân chủ phụ thuộc vào điều gì?|Mức độ và khả năng nhân dân tham gia công việc nhà nước, xã hội|Chỉ tên gọi của bộ máy nhà nước|Chỉ diện tích lãnh thổ quốc gia|Chỉ số lượng cơ quan hành chính|30:4
4|Hai giai đoạn ra đời dân chủ xã hội chủ nghĩa theo slide là gì?|Công nhân giành dân chủ, rồi dùng dân chủ tổ chức nhà nước mới|Nhà nước tư sản tự chuyển giao, rồi công nhân ngừng tổ chức|Công nhân xây nhà nước trước, rồi mới giành dân chủ|Chỉ cần tuyên bố dân chủ mà không có cách mạng|31:4
4|Bản chất chung của dân chủ xã hội chủ nghĩa theo slide hướng tới điều gì?|Thủ tiêu áp bức, giải phóng con người và bảo đảm quyền lực của nhân dân|Củng cố đặc quyền của giai cấp tư sản|Duy trì áp bức giữa các giai cấp|Loại bỏ mọi quyền tự do, bình đẳng|32:4
4|Mối quan hệ giữa dân chủ xã hội chủ nghĩa và pháp luật theo slide là gì?|Thống nhất biện chứng|Hoàn toàn tách rời|Pháp luật thay thế toàn bộ dân chủ|Dân chủ chỉ tồn tại khi không có pháp luật|34:4
4|Nhà nước xã hội chủ nghĩa ra đời từ cuộc cách mạng do ai tiến hành?|Giai cấp vô sản và nhân dân lao động dưới lãnh đạo của Đảng Cộng sản|Giai cấp tư sản và chủ nô dưới lãnh đạo phong kiến|Chỉ bộ máy hành chính cũ|Chỉ các tập đoàn kinh tế tư nhân|35:4
4|Phân loại chức năng nhà nước xã hội chủ nghĩa theo phạm vi tác động gồm gì?|Đối nội và đối ngoại|Kinh tế và văn hóa|Giai cấp và xã hội|Lập pháp và tư pháp|39:4
4|Phân loại chức năng nhà nước xã hội chủ nghĩa theo tính chất quyền lực gồm gì?|Chức năng giai cấp và chức năng xã hội|Chức năng đối nội và đối ngoại|Chức năng kinh tế và văn hóa|Chức năng lập pháp và hành pháp|39:4
4|Dân chủ xã hội chủ nghĩa là gì đối với hoạt động của nhà nước xã hội chủ nghĩa?|Cơ sở, nền tảng|Yếu tố không liên quan|Kết quả chỉ có sau khi nhà nước mất đi|Sự thay thế của toàn bộ pháp luật|40:4
4|Nhà nước xã hội chủ nghĩa là công cụ quan trọng để làm gì?|Thực thi quyền làm chủ của người dân|Duy trì độc quyền của tư sản|Loại bỏ sự tham gia của nhân dân|Thay thế mọi tổ chức chính trị - xã hội|40:4
4|Ở Việt Nam, dân chủ phải được thực hiện ở phạm vi nào theo slide?|Trong thực tiễn ở tất cả các cấp và mọi lĩnh vực|Chỉ ở cấp trung ương|Chỉ trong lĩnh vực kinh tế|Chỉ trong văn bản pháp luật|42:4
4|Theo slide, quyền lực nhà nước Việt Nam có quan hệ nào giữa ba nhánh?|Thống nhất với phân công, phối hợp và kiểm soát|Tách biệt tuyệt đối, không có phối hợp|Chỉ giao cho hành pháp|Không có cơ chế kiểm soát|44:4
4|Một điều kiện tiên quyết để xây dựng dân chủ xã hội chủ nghĩa Việt Nam là gì?|Xây dựng Đảng Cộng sản Việt Nam trong sạch, vững mạnh|Bãi bỏ mọi tổ chức chính trị - xã hội|Duy trì bộ máy nhà nước tư sản|Loại bỏ giám sát và phản biện xã hội|46:4
4|Giải pháp nào được slide nêu để xây dựng dân chủ ở Việt Nam?|Xây dựng đội ngũ cán bộ, công chức trong sạch, có năng lực|Giảm vai trò của pháp luật|Ngừng cải cách thể chế nhà nước|Không đấu tranh chống tham nhũng|47:4
1|Theo slide, cơ sở của gia đình trong xã hội mới là gì?|Bình đẳng và tự nguyện|Áp đặt và mục đích kinh tế|Đặc quyền của nam giới|Ràng buộc bằng địa vị dòng họ|30:1
1|Sau Công xã Pari, yêu cầu về Đảng theo slide là gì?|Gắn bó với quần chúng và được trang bị lý luận khoa học|Tách khỏi quần chúng và chỉ dựa vào kinh nghiệm|Chỉ hoạt động trong lĩnh vực kinh tế|Từ bỏ đoàn kết quốc tế|27:1
1|V.I. Lênin vận dụng chủ nghĩa xã hội khoa học trước Cách mạng Tháng Mười bằng việc nào?|Đấu tranh chống trào lưu phi Mác-xít và xây dựng lý luận về Đảng kiểu mới|Viết Tuyên ngôn của Đảng Cộng sản năm 1848|Tổng kết Công xã Pari cùng C. Mác|Phát hiện thuyết tế bào|31:1
1|Sau Cách mạng Tháng Mười, Lênin nghiên cứu những vấn đề xây dựng xã hội mới trên lĩnh vực nào?|Chính trị, kinh tế, văn hóa và giáo dục|Chỉ lĩnh vực quân sự|Chỉ lĩnh vực ngoại giao|Chỉ lĩnh vực khoa học tự nhiên|32:1
2|Theo slide, sứ mệnh công nhân Việt Nam được trình bày qua những thời kỳ nào?|Trước và sau Cách mạng Tháng Tám, rồi xây dựng và bảo vệ Tổ quốc xã hội chủ nghĩa|Chỉ thời kỳ trước Cách mạng Tháng Tám|Chỉ thời kỳ sau đổi mới|Chỉ thời kỳ thuộc địa trước thế kỷ XIX|21:2
3|Phương hướng kinh tế trong thời kỳ quá độ theo slide là gì?|Phát triển kinh tế thị trường định hướng xã hội chủ nghĩa|Bỏ hoàn toàn mọi quan hệ thị trường|Phát triển kinh tế tự cung tự cấp|Chỉ duy trì quan hệ sản xuất tư bản thống trị|19:3
4|Chế độ phong kiến tương ứng với hình thức chính trị nào trong sơ đồ slide?|Quân chủ phong kiến|Dân chủ tư sản|Dân chủ vô sản|Dân chủ chủ nô|24:4
4|Trong dân chủ xã hội chủ nghĩa, nhân dân giữ vai trò nào?|Chủ thể quyền lực nhà nước|Chỉ đối tượng bị quản lý|Chỉ lực lượng sản xuất vật chất|Chỉ người thực hiện nghĩa vụ kinh tế|33:4
4|Nhà nước xã hội chủ nghĩa theo slide có nhiệm vụ lịch sử nào?|Xây dựng thành công chủ nghĩa xã hội và đưa nhân dân lao động lên địa vị làm chủ|Duy trì nhà nước tư sản và tư hữu tuyệt đối|Khôi phục nhà nước phong kiến|Chỉ duy trì trật tự cũ mà không cải tạo xã hội|38:4
4|Phân loại chức năng nhà nước xã hội chủ nghĩa theo lĩnh vực tác động gồm gì?|Kinh tế, chính trị, văn hóa và xã hội|Chỉ đối nội và đối ngoại|Chỉ trấn áp và tổ chức xây dựng|Chỉ lập pháp và tư pháp|39:4
"""

def parse(raw, kind):
    result = []
    for row in raw.strip().splitlines():
        parts = [x.strip() for x in row.split("|")]
        if len(parts) != 7:
            raise ValueError((kind, row, len(parts)))
        chapter, prompt, correct, *rest = parts
        wrongs, ref = rest[:3], rest[3]
        if kind == "doc":
            line = int(ref)
            evidence = doc_lines[line - 1].strip()
            source = {"kind": "doc", "label": f"Ghi chú · dòng {line}", "url": DOC_URL, "evidence": evidence, "line": line}
        else:
            page, ch = map(int, ref.split(":"))
            record = slide_lookup[(ch, page)]
            source = {"kind": "slide", "label": f"Slide chương {ch} · trang {page}", "file": record["file"], "page": page, "evidence": record["text"]}
        idx = len(result)
        answer = (idx * 7 + idx // 4) % 4
        choices = wrongs.copy()
        choices.insert(answer, correct)
        result.append({
            "id": f"{kind}-{idx+1:03}", "chapter": int(chapter),
            "question": prompt, "choices": choices, "answer": answer,
            "explanation": f"Đáp án đúng: {correct}. Đối chiếu trực tiếp với đoạn nguồn bên cạnh.",
            "source": source
        })
    return result

questions = sorted(parse(DOC, "doc"), key=lambda q: q["source"]["line"]) + sorted(
    parse(SLIDE, "slide"), key=lambda q: (q["chapter"], q["source"]["page"])
)

exam_forms = []
for form_index, form in enumerate(EXAM_FORMS, 1):
    ids = []
    rows = form.strip().splitlines()
    assert len(rows) == 30, f"Đề {form_index} không đủ 30 câu"
    for row in rows:
        parts = [part.strip() for part in row.split("|")]
        assert len(parts) == 7, row
        ref, prompt, correct, w1, w2, w3, rationale = parts
        if ref.startswith("D"):
            line = int(ref[1:])
            assert 1 <= line <= len(doc_lines)
            chapter = 1 if line < 9 else 2 if line < 35 else 3 if line < 64 else 4
            source = {
                "kind": "doc", "label": f"Ghi chú · dòng {line}", "url": DOC_URL,
                "evidence": doc_lines[line - 1].strip(), "line": line
            }
        else:
            ch, page = map(int, ref[1:].split(":"))
            record = slide_lookup[(ch, page)]
            chapter = ch
            source = {
                "kind": "slide", "label": f"Slide chương {ch} · trang {page}",
                "file": record["file"], "page": page, "evidence": record["text"]
            }
        seq = len(questions) - len(parse(DOC, "doc")) - len(parse(SLIDE, "slide"))
        qid = f"extra-{seq + 1:03}"
        answer = (seq * 7 + seq // 4 + form_index) % 4
        choices = [w1, w2, w3]
        choices.insert(answer, correct)
        assert len(set(choices)) == 4, qid
        questions.append({
            "id": qid, "chapter": chapter, "question": prompt,
            "choices": choices, "answer": answer, "explanation": rationale,
            "source": source, "exam": form_index
        })
        ids.append(qid)
    themes = [
        ("Ghi chú trọng tâm", "Ưu tiên ý trong ghi chú, thêm các câu đối chiếu slide"),
        ("Slide chuyên sâu", "Khai thác lập luận và chi tiết từ slide bài giảng"),
        ("Tổng hợp phân biệt", "Trộn hai nguồn, chú trọng phương án gần đúng")
    ]
    title, focus = themes[form_index - 1]
    exam_forms.append({
        "id": f"midterm-{form_index}", "title": f"Đề {form_index} · {title}",
        "focus": focus, "durationSeconds": 15 * 60, "questionIds": ids
    })

# The next five forms use the original sourced bank. Pin IDs to keep saved
# attempts valid when data.json is regenerated, then mix chapters in each form.
base_by_id = {q["id"]: q for q in questions if not q["id"].startswith("extra-")}
for form_index, raw_ids in enumerate(MORE_EXAM_IDS, 4):
    ids = raw_ids.split()
    assert len(ids) == len(set(ids)) == 30, f"Đề {form_index} phải có 30 câu riêng"
    assert all(qid in base_by_id for qid in ids), f"Đề {form_index} có ID lạ"
    assert {base_by_id[qid]["chapter"] for qid in ids} == {1, 2, 3, 4}
    assert {base_by_id[qid]["source"]["kind"] for qid in ids} == {"doc", "slide"}
    random.Random(20261020 + form_index).shuffle(ids)
    exam_forms.append({
        "id": f"midterm-{form_index}",
        "title": f"Đề {form_index} · Tổng hợp bốn chương",
        "focus": "Trộn ghi chú và slide; kiểm tra đủ bốn chương bằng nhiều kiểu câu hỏi.",
        "durationSeconds": 15 * 60,
        "questionIds": ids,
    })

# Keep all angles of the same source statement together in practice mode.
questions.sort(key=lambda q: (
    0 if q["source"]["kind"] == "doc" else 1,
    q["source"].get("line", q["chapter"]),
    q["source"].get("page", 0),
    0 if not q["id"].startswith("extra-") else 1,
    q["id"]
))

assert len({q["id"] for q in questions}) == len(questions)
assert all(len(q["choices"]) == 4 and len(set(q["choices"])) == 4 for q in questions)
assert len(exam_forms) == 8 and all(len(f["questionIds"]) == 30 for f in exam_forms)
all_exam_ids = [qid for form in exam_forms for qid in form["questionIds"]]
assert len(all_exam_ids) == len(set(all_exam_ids)), "Các đề không được lặp câu hỏi"
public = ROOT / "dist"
public.mkdir(exist_ok=True)
(public / "data.json").write_text(json.dumps({
    "questions": questions,
    "examForms": exam_forms,
    "docLines": doc_lines,
    "slidePages": slides,
    "docUrl": DOC_URL,
}, ensure_ascii=False), encoding="utf-8")
print(f"{len(questions)} questions: {len(parse(DOC, 'doc'))} original doc, {len(parse(SLIDE, 'slide'))} original slide, 90 new")
