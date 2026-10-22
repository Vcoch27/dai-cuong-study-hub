# Đại cương study hub

Kho ôn tập môn đại cương, bắt đầu với **Chủ nghĩa xã hội khoa học** cho kỳ thi giữa kỳ dạng trắc nghiệm.

## Chuyển môn và khung Tư tưởng Hồ Chí Minh

Thanh chọn môn ở đầu trang chuyển giữa CNXHKH (`/`) và Tư tưởng Hồ Chí Minh
(`/?course=hcm`). Tiến trình, câu lưu và kết quả đề được lưu riêng cho mỗi môn.
Môn HCM hiện có **120 câu** (30 câu chương 1, 90 câu chương 2), bốn đề tổng hợp
30 câu/15 phút và đủ văn bản của 62 trang nguồn trong phần đọc học liệu.
Văn bản do người học trích xuất được nhận trực tiếp, không cần phân tích lại slide.
Xem `content/hcm/README.md` về cách bổ sung nguồn và câu hỏi, sau đó chạy
`python compile_hcm_bank.py`, `python build_hcm_data.py` và `python audit_hcm_data.py`.
Các chế độ luyện tập, đọc nguồn, luyện lại câu sai
và đề 30 câu/15 phút dùng chung giao diện hiện tại khi có dữ liệu thực.

## Nội dung

### Ngân hàng HCM từ sáu tập

Trang `/?course=hcm&track=bank` chạy song song với phần ôn theo slide, có liên kết
chuyển qua lại. Từ 261 vị trí nguồn đã gộp còn 139 mục duy nhất: 133 trắc nghiệm,
bốn câu cần đối chiếu, hai tự luận. Đã thêm nhiễu cho 23 mục chỉ có câu trả lời.
Có chế độ toàn bộ không lặp, sáu tập, các phần/nhóm của tập 1–2, tìm kiếm,
lưu câu và làm lại. Câu xuất hiện ở nhiều tập dùng chung tiến trình; tiến trình
ngân hàng tách riêng với phần theo slide và CNXHKH. Xem `content/hcm-bank/README.md`.

### CNXHKH

- 92 câu từ [tài liệu ghi chú Google Docs](https://docs.google.com/document/d/1iKcT1_tLk5xTTdsBzRmLEv-KpymeBbIbQSkn5-98F-A/edit), ưu tiên học trước.
- 67 câu từ bốn bộ slide chương 1–4, ôn sau phần ghi chú.
- 90 câu mới hỏi theo nhiều hướng từ cùng một ý: hỏi ngược, phân biệt mốc/khái niệm, ngoại lệ và chọn đáp án đúng nhất. Tổng ngân hàng hiện có **249 câu**.
- Toàn bộ 249 câu đã được biên tập lại phương án và giải thích: nhiễu cùng chủ đề, kiểm tra nhầm điều kiện/vai trò/phạm vi, giảm gợi ý từ từ ngữ tuyệt đối và độ dài. Nội dung hiện dùng nằm trong `reviewed_questions.py`; các đoạn câu hỏi ban đầu trong trình dựng chỉ giữ ID và ánh xạ nguồn. Mỗi lần dựng phải có đủ 249 bản biên tập.
- Trong chế độ luyện tập, các câu cùng đoạn ghi chú hoặc cùng trang slide được xếp cạnh nhau để luyện một ý theo nhiều góc nhìn.
- Tám đề giữa kỳ cố định: ba đề chuyên biệt và năm đề tổng hợp từ cả ghi chú lẫn slide, đủ bốn chương. Mỗi đề 30 câu trong 15 phút; 240 câu không lặp giữa các đề. Bài tự nộp khi hết giờ; đáp án và nguồn chỉ hiện sau khi nộp. Có thể làm lại và xem điểm gần nhất, điểm cao nhất.
- Mỗi câu có bốn lựa chọn, đáp án hiện ngay khi chọn và đoạn nguồn đối chiếu bên cạnh.
- Chế độ đọc giữ đầy đủ văn bản trích xuất từ tài liệu ghi chú và 125 trang slide.
- Với câu lấy từ slide, cột đối chiếu hiện ảnh đúng trang PowerPoint gốc sau khi trả lời. Có thể phóng to, xem trang trước/sau và mở ảnh gốc; phần văn bản nằm trong mục thu gọn. Khi làm lại hoặc chưa nộp đề, ảnh nguồn được ẩn. Chế độ đọc có ảnh đủ 125 trang.
- Tìm kiếm, lọc chương, xem câu sai, lưu câu và ghi nhớ tiến độ bằng localStorage.
- Có thể làm lại từng câu, luyện lại câu sai hoặc làm lại nhóm đang lọc. Tiến độ “đã làm” được giữ riêng với câu trả lời của lượt luyện; kết quả gần nhất cập nhật danh sách câu sai. Khi luyện lại, đáp án, giải thích và đoạn nguồn đều được ẩn. Nhóm câu sai giữ nguyên trong lượt ôn để đọc được phản hồi sau khi sửa đúng; chọn lại bộ lọc “Làm sai” để lấy danh sách mới nhất.
- Chọn đáp án giữ nguyên vị trí cuộn; chuyển câu bằng nút, danh sách số hoặc phím mũi tên đưa đầu khung câu hỏi vào màn hình. Các cột giữ vị trí riêng; trong đề thi, thanh đồng hồ bám theo vùng làm bài.
- Lượt luyện với câu hỏi đã biên tập được lưu riêng. Câu đánh dấu được chuyển sang bản mới; dữ liệu bản cũ giữ nguyên trên thiết bị. Điểm cao nhất của đề cũ có nhãn “Trước biên tập”, không gộp với điểm bản mới.

## Chạy tại máy

Sử dụng server tĩnh tại thư mục `dist`:

```powershell
python -m http.server 4173 -d dist
```

Mở `http://localhost:4173`. Để tạo lại dữ liệu sau khi chỉnh câu hỏi, chạy `python build_data.py`.

Ảnh trong `dist/slides/` được xuất trực tiếp từ PowerPoint gốc rồi mã hóa WebP, không dựng lại bố cục. Nếu thay bộ slide, chạy trên Windows có PowerPoint và Python Pillow:

```powershell
powershell -NoProfile -File render_slides.ps1
python pack_slide_images.py
python build_data.py
```

Trình dựng kiểm tra dấu vân tay của bộ slide, số trang và từng ảnh để tránh gắn nhầm ảnh sau khi đổi tài liệu. Thư mục ảnh PNG trung gian `.slide-renders/` không đưa lên Git.

Kiểm tra sau khi sửa ngân hàng hoặc cách lưu tiến độ:

```powershell
python build_data.py
python audit_questions.py
node --experimental-vm-modules tests/progress-smoke.mjs
```

`audit_questions.py` kiểm tra nguồn, ID, bốn lựa chọn, cấu trúc tám đề, từ dễ lộ ở phương án nhiễu và chênh lệch độ dài. Sau biên tập, chiến thuật chọn phương án dài nhất đạt 24,16%, ngắn nhất đạt 25,17% trên ngân hàng (chọn đều khi bằng độ dài), so với 25% kỳ vọng khi đoán ngẫu nhiên. Đây là kiểm tra gợi ý hình thức, không phải phép đo độ khó học thuật của từng câu. Tính đúng duy nhất và chất lượng nhiễu vẫn cần biên tập theo nguồn.

## Nguồn và phạm vi

Tài liệu gốc nằm trong `sources/` và `slidegk/`. Trường `source` của mỗi câu trong `dist/data.json` giữ nhãn nguồn, dòng hoặc trang slide và đoạn văn trích xuất. Bộ câu hỏi phản ánh nội dung tài liệu lớp học; các phát biểu mang tính học thuật trong tài liệu không phải ý kiến độc lập của ứng dụng.

Lưu ý: văn bản trích xuất có thể thiếu phần chữ trong ảnh hoặc sơ đồ. Ảnh trang slide gốc được hiển thị trong phần đối chiếu và chế độ đọc để xem đầy đủ bố cục, hình ảnh.
