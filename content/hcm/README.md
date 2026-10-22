# Tư tưởng Hồ Chí Minh — nhận nội dung văn bản

Phạm vi hiện tại: chương 1, 2 và 3. Giao diện nằm tại `/?course=hcm`.
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
## Nội dung đã xuất bản

### Bổ sung chương 3

- Nguồn đợt mới: `source-chapters-3-4.md` giữ nguyên tệp nhận từ người học;
  trình nhập `import_hcm_chapter3.py` chỉ lấy chương 3, bỏ chương 4 khỏi dữ liệu học.
- Giữ đủ 69 trang chương 3 trong phần đọc, kể cả trang minh họa hoặc có chữ mờ.
- `authored_chapter3.txt`: 120 câu, có nguồn đối chiếu từ 53 trang lý thuyết;
  14 cơ bản, 90 phân biệt, 16 vận dụng. Những trang minh họa hoặc nội dung lặp
  vẫn đọc được nhưng không ép thành câu hỏi ghi nhớ hình ảnh.
- Bốn đề chương 3, 30 câu/900 giây; đủ 120 câu không trùng ID giữa bốn đề.
  Phân bổ xen kẽ các chủ đề, không chia mỗi đề thành một phần đầu/cuối chương.
- Tổng hiện tại: 240 câu, 131 trang đọc, tám đề. Chương 1–2, bốn đề cũ,
  ID, thứ tự lựa chọn, phiên bản dữ liệu và khóa tiến trình giữ nguyên.
- Không thay đổi ngân hàng HCM từ sáu tập; đó là tuyến học riêng.

### Đợt chương 1–2 (giữ nguyên)

- Nguồn: `source.md`, bản văn bản người học cung cấp ngày 22/10/2026.
- `content.json`: đủ 62 trang văn bản (8 trang chương 1, 54 trang chương 2).
- `authored_questions.txt`: 120 câu biên soạn, 30 câu chương 1 và 90 câu chương 2.
- `questions.json`: lựa chọn đã trộn, ID và bốn đề cố định, mỗi đề 30 câu/900 giây.
- 120 câu không lặp ID giữa bốn đề. Câu cùng trang có thể kiểm tra các góc kiến thức khác nhau.
- Phần đọc giữ cả các trang minh họa. Các chi tiết cần tránh và phạm vi kiểm tra nằm trong `editorial-notes.md`.

Sau khi sửa nội dung biên soạn, chạy:

```powershell
python compile_hcm_bank.py
python build_hcm_data.py
python audit_hcm_data.py
node --experimental-vm-modules tests/progress-smoke.mjs
```

Trình biên dịch giữ thứ tự lựa chọn của câu có cùng ID và cùng tập lựa chọn,
đồng thời giữ đề đã tồn tại. Không chèn/đảo dòng cũ trong tệp biên soạn:
ID hiện được cấp theo thứ tự trong từng chương. Khi mở rộng đợt sau, cần cấp ID
mới rõ ràng và thêm đề riêng, tránh thay đổi các đề đang có người làm.

Để nhập lại văn bản chương 3, chạy `python import_hcm_chapter3.py` trước các
lệnh trên. Không đổi thứ tự các dòng đã xuất bản trong `authored_chapter3.txt`.
