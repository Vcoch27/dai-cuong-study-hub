# Đại cương study hub

Kho ôn tập môn đại cương, bắt đầu với **Chủ nghĩa xã hội khoa học** cho kỳ thi giữa kỳ dạng trắc nghiệm.

## Nội dung

- 92 câu từ [tài liệu ghi chú Google Docs](https://docs.google.com/document/d/1iKcT1_tLk5xTTdsBzRmLEv-KpymeBbIbQSkn5-98F-A/edit), ưu tiên học trước.
- 67 câu từ bốn bộ slide chương 1–4, ôn sau phần ghi chú.
- 90 câu mới hỏi theo nhiều hướng từ cùng một ý: hỏi ngược, phân biệt mốc/khái niệm, ngoại lệ và chọn đáp án đúng nhất. Tổng ngân hàng hiện có **249 câu**.
- Toàn bộ 249 câu đã được biên tập lại phương án và giải thích: nhiễu cùng chủ đề, kiểm tra nhầm điều kiện/vai trò/phạm vi, giảm gợi ý từ từ ngữ tuyệt đối và độ dài. Nội dung hiện dùng nằm trong `reviewed_questions.py`; các đoạn câu hỏi ban đầu trong trình dựng chỉ giữ ID và ánh xạ nguồn. Mỗi lần dựng phải có đủ 249 bản biên tập.
- Trong chế độ luyện tập, các câu cùng đoạn ghi chú hoặc cùng trang slide được xếp cạnh nhau để luyện một ý theo nhiều góc nhìn.
- Tám đề giữa kỳ cố định: ba đề chuyên biệt và năm đề tổng hợp từ cả ghi chú lẫn slide, đủ bốn chương. Mỗi đề 30 câu trong 15 phút; 240 câu không lặp giữa các đề. Bài tự nộp khi hết giờ; đáp án và nguồn chỉ hiện sau khi nộp. Có thể làm lại và xem điểm gần nhất, điểm cao nhất.
- Mỗi câu có bốn lựa chọn, đáp án hiện ngay khi chọn và đoạn nguồn đối chiếu bên cạnh.
- Chế độ đọc giữ đầy đủ văn bản trích xuất từ tài liệu ghi chú và 125 trang slide.
- Tìm kiếm, lọc chương, xem câu sai, lưu câu và ghi nhớ tiến độ bằng localStorage.
- Lượt luyện với câu hỏi đã biên tập được lưu riêng. Câu đánh dấu được chuyển sang bản mới; dữ liệu bản cũ giữ nguyên trên thiết bị. Điểm cao nhất của đề cũ có nhãn “Trước biên tập”, không gộp với điểm bản mới.

## Chạy tại máy

Sử dụng server tĩnh tại thư mục `dist`:

```powershell
python -m http.server 4173 -d dist
```

Mở `http://localhost:4173`. Để tạo lại dữ liệu sau khi chỉnh câu hỏi, chạy `python build_data.py`.

Kiểm tra sau khi sửa ngân hàng hoặc cách lưu tiến độ:

```powershell
python build_data.py
python audit_questions.py
node --experimental-vm-modules tests/progress-smoke.mjs
```

`audit_questions.py` kiểm tra nguồn, ID, bốn lựa chọn, cấu trúc tám đề, từ dễ lộ ở phương án nhiễu và chênh lệch độ dài. Sau biên tập, chiến thuật chọn phương án dài nhất đạt 24,16%, ngắn nhất đạt 25,17% trên ngân hàng (chọn đều khi bằng độ dài), so với 25% kỳ vọng khi đoán ngẫu nhiên. Đây là kiểm tra gợi ý hình thức, không phải phép đo độ khó học thuật của từng câu. Tính đúng duy nhất và chất lượng nhiễu vẫn cần biên tập theo nguồn.

## Nguồn và phạm vi

Tài liệu gốc nằm trong `sources/` và `slidegk/`. Trường `source` của mỗi câu trong `dist/data.json` giữ nhãn nguồn, dòng hoặc trang slide và đoạn văn trích xuất. Bộ câu hỏi phản ánh nội dung tài liệu lớp học; các phát biểu mang tính học thuật trong tài liệu không phải ý kiến độc lập của ứng dụng.

Lưu ý: nội dung trong slide có trang chỉ gồm hình, sơ đồ hoặc yêu cầu thảo luận. Chế độ đọc chứa văn bản có thể trích xuất được; xem file PowerPoint gốc để đối chiếu hình ảnh.
