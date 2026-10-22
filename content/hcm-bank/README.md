# Ngân hàng câu hỏi HCM độc lập với phần học theo slide

Đường dẫn: `/?course=hcm&track=bank`. Phần học theo slide giữ tại `/?course=hcm`.

## Nguồn và kết quả nhập

`source.txt` là bản sao nguyên trạng tệp người học gửi. Hướng dẫn biên soạn nằm
trong yêu cầu của người học; các dòng quy ước trong nguồn chỉ là mô tả tài liệu.
Không coi đáp án hoặc nhận định trong tài liệu ôn tập là khóa thi chính thức.

- 261 vị trí nguồn: 236 trắc nghiệm có lựa chọn nhưng không có khóa chấm,
  23 câu có sẵn câu trả lời, hai tự luận.
- 139 mục duy nhất: 133 trắc nghiệm có đáp án biên tập, bốn mục cần đối chiếu,
  hai tự luận có gợi ý, không chấm tự động.
- 122 lần xuất hiện lặp được gộp bằng quyết định biên tập rõ ràng; không dùng
  độ giống văn bản để tự xóa câu. Những câu hỏi khác góc kiểm tra vẫn được giữ.
- Tập 1 có hai phần; tập 2 có ba nhóm, kể cả câu số 00 và các khoảng số bị khuyết.
  Các tập 3–6 giữ tên trong nguồn. Mỗi tập/nhóm theo thứ tự xuất hiện gốc.
- Một câu có nhiều nguồn dùng một ID, được hiện trong từng tập chứa nó.
  Chế độ toàn bộ hiện đúng một lần. Mục đọc câu gốc giữ đủ 261 vị trí để đối chiếu.

| Tập | Vị trí trong file | Mục không lặp trong tập |
|---|---:|---:|
| 1 | 44 | 43 |
| 2 | 68 | 67 |
| 3 | 57 | 54 |
| 4 | 50 | 50 |
| 5 | 17 | 17 |
| 6 | 25 | 25 |

Không cộng cột cuối để tính toàn bộ: nhiều câu thuộc nhiều tập.

## Biên tập và đáp án

`editorial.py` liệt kê từng câu chuẩn, tất cả ID nguồn gộp vào nó, đáp án,
giải thích, tham khảo và điều chỉnh có chủ đích. Nhiễu mới cho 23 câu trả lời
ngắn được viết cùng trường nghĩa, không thêm từ tuyệt đối để lộ phương án sai.
Lựa chọn đúng được trộn với hạt giống cố định. Hai câu hỏi tên quốc gia có độ dài
tên riêng chênh nhau tự nhiên, không kéo dài câu bằng từ thừa để qua kiểm tra.

Với trắc nghiệm đã có lựa chọn, giữ bộ lựa chọn của câu đại diện, sửa lỗi OCR rõ
ràng. Một số câu cần khôi phục chỗ trống hoặc làm rõ tiêu chí; ghi chú hiển thị
trong nguồn. Câu và lựa chọn gốc luôn được giữ nguyên trong `occurrences`.
Đáp án do biên tập bổ sung được phân biệt với đáp án đúng đã có trong nguồn.
Các trang tham khảo chính thức hoặc nội dung lớp được gắn khi có đối chiếu.

Bốn mục không chấm tự động:

1. `bank-happiness-quote-ambiguous`: trích dẫn về độc lập và hạnh phúc có nhiều
   mức khái quát đúng trong các lựa chọn; câu dẫn chưa quy định tiêu chí.
2. `bank-basis-ambiguous`: hỏi chung cơ sở hình thành nhưng trộn nhiều loại cơ sở.
3. `bank-many-translations-ambiguous`: nhiều tác phẩm được dịch sang nhiều thứ tiếng.
4. `bank-first-complete-definition-ambiguous`: trộn các tiêu chí lần đầu, hoàn chỉnh,
   Điều lệ và các mốc Đại hội VII/IX/XI.

Mọi mục đều xem được theo tập và toàn bộ. Mục chưa đủ căn cứ không được gán
một đáp án đoán để chấm; phần hướng dẫn giải thích chỗ cần đối chiếu. Tự luận
có gợi ý, không ép thành một đáp án A/B/C/D. Hai loại này không tăng số câu
trắc nghiệm đã làm. Tiến trình riêng dùng khóa `dai-cuong-hcm-bank-v1`.

## Dựng và kiểm tra

```powershell
python import_hcm_bank.py
python build_hcm_bank.py
python audit_hcm_bank.py
node --experimental-vm-modules tests/progress-smoke.mjs
```

Importer nhận tệp văn bản định dạng sẵn, không đọc lại PDF. Trình dựng không tự
tìm đáp án; mọi quyết định nằm trong manifest biên tập. ID theo chủ đề ổn định.
Khi sửa khóa, lựa chọn hoặc cách gộp của câu đã xuất bản, cần xem xét ảnh hưởng
tiến trình trước khi đổi dữ liệu.

Audit kiểm tra nguồn nguyên vẹn, mỗi nguồn được gán đúng một lần, nhóm/tập,
đáp án, bốn lựa chọn và ranh giới chấm điểm. Với 23 câu bổ sung nhiễu, chiến thuật
chọn câu dài nhất đạt 26,09%, ngắn nhất 28,26% khi chia đều trường hợp bằng độ
dài. Đây không phải kiểm định độ khó học thuật. Không áp các con số này cho
toàn bộ câu gốc vốn giữ lựa chọn của tài liệu.
