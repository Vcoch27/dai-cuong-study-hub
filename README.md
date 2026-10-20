# Đại cương study hub

Kho ôn tập môn đại cương, bắt đầu với **Chủ nghĩa xã hội khoa học** cho kỳ thi giữa kỳ dạng trắc nghiệm.

## Nội dung

- 92 câu từ [tài liệu ghi chú Google Docs](https://docs.google.com/document/d/1iKcT1_tLk5xTTdsBzRmLEv-KpymeBbIbQSkn5-98F-A/edit), ưu tiên học trước.
- 67 câu từ bốn bộ slide chương 1–4, ôn sau phần ghi chú.
- 90 câu mới hỏi theo nhiều hướng từ cùng một ý: hỏi ngược, phân biệt mốc/khái niệm, ngoại lệ và chọn đáp án đúng nhất. Tổng ngân hàng hiện có **249 câu**.
- Trong chế độ luyện tập, các câu cùng đoạn ghi chú hoặc cùng trang slide được xếp cạnh nhau để luyện một ý theo nhiều góc nhìn.
- Tám đề giữa kỳ cố định: ba đề chuyên biệt và năm đề tổng hợp từ cả ghi chú lẫn slide, đủ bốn chương. Mỗi đề 30 câu trong 15 phút; 240 câu không lặp giữa các đề. Bài tự nộp khi hết giờ; đáp án và nguồn chỉ hiện sau khi nộp. Có thể làm lại và xem điểm gần nhất, điểm cao nhất.
- Mỗi câu có bốn lựa chọn, đáp án hiện ngay khi chọn và đoạn nguồn đối chiếu bên cạnh.
- Chế độ đọc giữ đầy đủ văn bản trích xuất từ tài liệu ghi chú và 125 trang slide.
- Tìm kiếm, lọc chương, xem câu sai, lưu câu và ghi nhớ tiến độ bằng localStorage.

## Chạy tại máy

Sử dụng server tĩnh tại thư mục `dist`:

```powershell
python -m http.server 4173 -d dist
```

Mở `http://localhost:4173`. Để tạo lại dữ liệu sau khi chỉnh câu hỏi, chạy `python build_data.py`.

## Nguồn và phạm vi

Tài liệu gốc nằm trong `sources/` và `slidegk/`. Trường `source` của mỗi câu trong `dist/data.json` giữ nhãn nguồn, dòng hoặc trang slide và đoạn văn trích xuất. Bộ câu hỏi phản ánh nội dung tài liệu lớp học; các phát biểu mang tính học thuật trong tài liệu không phải ý kiến độc lập của ứng dụng.

Lưu ý: nội dung trong slide có trang chỉ gồm hình, sơ đồ hoặc yêu cầu thảo luận. Chế độ đọc chứa văn bản có thể trích xuất được; xem file PowerPoint gốc để đối chiếu hình ảnh.
