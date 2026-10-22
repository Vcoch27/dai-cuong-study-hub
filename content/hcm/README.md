# Tư tưởng Hồ Chí Minh — nhận nội dung văn bản

Phạm vi hiện tại: chương 1 và 2. Giao diện nằm tại `/?course=hcm`.
Người học gửi nội dung đã trích xuất trong chat hoặc dưới dạng tệp văn bản;
không cần đúng khuôn JSON. Giữ tiêu đề chương, mục và số trang nếu có.
Không cần phân tích lại PDF/PowerPoint.

## Khi nhận nội dung

1. Chia nội dung thành các đơn vị kiến thức trong `content.json`, giữ nguyên
   văn bản gốc trong `text`, gán ID ổn định. Mỗi mục thuộc một chương.
2. Biên soạn câu hỏi theo `writing-block.md` và các yêu cầu biên tập đã thống nhất:
   hỏi trực tiếp kiến thức; không dẫn “theo slide/ghi chú”; nhiễu gần nghĩa;
   không lộ đáp án qua từ tuyệt đối, độ dài hoặc phương án không liên quan.
3. Thêm các câu hỏi vào `questions.json`. Mỗi câu trỏ đến `sectionId` của
   đúng đoạn gốc. Một mục có thể có nhiều câu kiểm tra các khía cạnh khác nhau.
4. Kiểm tra tính đúng duy nhất và giải thích, rồi chạy `python build_hcm_data.py`.
   Trình dựng ghép dữ liệu, kiểm tra tham chiếu và xuất `dist/hcm-data.json`;
   không tự sinh câu hỏi hay suy diễn nội dung chưa được cung cấp.
5. Tạo các đề 30 câu / 900 giây sau khi ngân hàng đủ câu. Giữ ID câu, ID đề,
   thứ tự lựa chọn của câu đã xuất bản và `questionRevision` ổn định khi bổ sung,
   để giữ tiến trình. Nếu sửa tính đúng sai của câu cũ, cần kế hoạch chuyển dữ liệu.

## Định dạng nội bộ

Một phần tử của `content.json` → `sections`:

```json
{
  "id": "hcm-c1-m1-y1",
  "chapter": 1,
  "title": "Tên mục do nội dung gốc xác định",
  "page": 2,
  "text": "Văn bản nguồn do người học cung cấp, giữ nguyên để đối chiếu."
}
```

`page` không bắt buộc; không đoán số trang khi người học không cung cấp.

Một phần tử của `questions.json` → `questions`:

```json
{
  "id": "hcm-c1-q001",
  "sectionId": "hcm-c1-m1-y1",
  "question": "Câu hỏi hoàn chỉnh đã biên tập?",
  "choices": ["Phương án A", "Phương án B", "Phương án C", "Phương án D"],
  "answer": 2,
  "explanation": "Giải thích đáp án đúng và sự khác biệt với phương án nhiễu."
}
```

`answer` là chỉ số 0–3. Chương, nhãn và trích dẫn nguồn được lấy từ `sectionId`.
Đây là ví dụ cấu trúc, không phải câu hỏi được xuất bản.

Một phần tử của `examForms` gồm `id` (bắt đầu `hcm-`), `title`, `focus`,
`durationSeconds: 900` và `questionIds` (30 ID không trùng nhau).

Môn HCM dùng khóa lưu riêng `dai-cuong-hcm-v1`; CNXHKH giữ nguyên khóa cũ.
Hiện hai danh sách nguồn/câu hỏi đều trống theo yêu cầu chờ văn bản mới.
