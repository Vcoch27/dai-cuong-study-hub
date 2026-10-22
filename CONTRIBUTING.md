# Đóng góp cho Đại cương VKU

Có thể gửi tài liệu hoặc câu hỏi mà không cần viết code. Dữ liệu cần được rà trước khi xuất bản lên website.

## 1. Có thể đóng góp những gì?

- Slide PDF/PowerPoint, ghi chú hoặc văn bản đã trích xuất, có tên môn và chương.
- Bộ câu hỏi/đề năm trước, giữ tên tập, thứ tự câu và A–D trong bản gốc.
- Đáp án có căn cứ, giải thích, phương án nhiễu cho câu chỉ có câu trả lời.
- Sửa lỗi kiến thức, câu trùng, đáp án chồng lấn hoặc liên kết nhầm trang slide.
- Tài liệu cho môn đại cương mới; mở môn mới còn cần tích hợp giao diện, dữ liệu và khóa tiến trình.

## 2. Gửi qua Issue — không cần biết code

1. Mở [mẫu đóng góp dữ liệu](https://github.com/Vcoch27/dai-cuong-vku-study-hub/issues/new?template=data-contribution.yml).
2. Ghi môn, chương, lớp/học kỳ hoặc phiên bản tài liệu nếu biết.
3. Kéo tệp vào ô nội dung hoặc dẫn liên kết đọc được.
4. Nói rõ bản gốc, bản trích, câu tự soạn hay câu phục dựng từ ảnh; chỉ rõ phần chữ mờ.
5. Ghi nguồn của đáp án. Nếu chưa xác nhận, ghi **chưa xác nhận** thay vì đánh dấu một suy đoán thành đáp án chính thức.

Báo câu sai bằng [mẫu sửa câu hỏi/trang nguồn](https://github.com/Vcoch27/dai-cuong-vku-study-hub/issues/new?template=question-correction.yml), kèm nội dung hoặc ảnh giúp nhận diện câu và căn cứ đề nghị sửa.

Website chưa có chức năng tự tải dữ liệu lên. Issue là nơi gửi để người duy trì rà và tích hợp, không tự động tạo câu hỏi trên web.

## 3. Chuẩn bị nội dung

Sao chép [mẫu câu hỏi](contributions/question-template.md), lưu dạng Markdown/TXT UTF-8. Với PR dữ liệu thô, đặt tại `contributions/<ten-mon>/<ten-bo>.md` và kèm tệp nguồn hoặc liên kết đọc được.

Mỗi câu nên có:

| Trường | Nội dung cần gửi |
| --- | --- |
| Môn, chương, mục | Phạm vi kiến thức |
| Câu hỏi | Hỏi trực tiếp; tránh “theo slide/ghi chú” trong câu dẫn |
| Bốn lựa chọn | A–D cùng chủ đề, cần phân biệt kiến thức để chọn |
| Đáp án | Một đáp án đúng nhất hoặc ghi chưa xác nhận |
| Giải thích | Vì sao đúng; phương án khác sai/thiếu ở đâu |
| Nguồn | Tên tệp, chương, trang PDF/slide gốc và trích đoạn căn cứ |
| Mức đối chiếu | Trực tiếp, chỉ liên quan hoặc chưa tìm thấy |
| Ghi chú | Phục dựng, chữ mờ, câu trùng, năm/đề, hiệu đính với bản gốc |

**Đếm trang PDF từ 1, kể cả bìa.** Nếu số in trên slide khác thứ tự PDF, ghi cả hai. Một trang cùng chủ đề chưa chắc có chi tiết cần chấm.

Với văn bản slide, giữ ranh giới chương/trang, các ý nhỏ, trích dẫn và nội dung sơ đồ. Ghi `[CHƯA ĐỌC RÕ]` ở phần không chắc chắn. Gửi kèm bản trích xuất nếu có để giảm thời gian xử lý.

Đọc [writing-block.md](writing-block.md) trước khi biên soạn. Tránh nhiễu vô lý, từ tuyệt đối dễ loại trừ hoặc đáp án đúng nổi bật vì dài hơn ba lựa chọn còn lại.

## 4. Gửi Pull Request

1. Fork [repo](https://github.com/Vcoch27/dai-cuong-vku-study-hub), clone fork và tạo nhánh rõ mục đích, ví dụ `data/hcm-chuong-3`.
2. Thêm bản thô vào `contributions/`, hoặc sửa đúng tệp nguồn nếu đã tích hợp.
3. Mô tả nguồn, phạm vi, số câu thêm/sửa, cách gộp trùng và điểm chưa xác nhận.
4. Nếu sửa dữ liệu đang hoạt động, dựng lại và chạy kiểm tra liên quan ở mục 5.
5. Mở PR về `master`. PR dữ liệu thô ghi **chưa tích hợp vào website**; không bắt buộc tự sửa trình dựng.

### Tệp cần sửa khi tích hợp

| Phần | Nguồn chính | Trình dựng |
| --- | --- | --- |
| CNXHKH | `reviewed_questions.py`, các tệp đề và dựng hiện có | `build_data.py` |
| HCM theo slide | `content/hcm/content.json`, `authored_questions.txt`, `authored_chapter3.txt` | `compile_hcm_bank.py`, `build_hcm_data.py` |
| Sáu tập HCM | `content/hcm-bank/source.txt`, `imported.json`, `editorial.py` | `import_hcm_bank.py`, `build_hcm_bank.py` |
| Đề năm trước 1 | `content/hcm-bank/past-exam-1.txt`, `extend_hcm_past_exam.py` | `build_hcm_bank.py` |
| Ảnh HCM | `sources/hcm/`, manifest trang | `render_hcm_slides.py` |
| Đối chiếu ngân hàng | `content/hcm-bank/slide-review.txt`, quyết định trong `extend_hcm_past_exam.py` | `build_hcm_bank.py`, `audit_hcm_slide_links.py` |

`dist/*-data.json` là đầu ra: sửa nguồn rồi dựng lại, tránh chỉ sửa JSON phát hành. Không cần dựng lại ảnh nếu chỉ sửa câu chữ/giải thích.

Các bộ hiện tại có kiểm tra số câu, đề và nguồn cố định. Thêm bộ mới cần cập nhật bộ nhập, ánh xạ và kiểm tra tương ứng; chép tệp vào thư mục chưa có nghĩa đã tích hợp. Có thể gửi dữ liệu thô để người duy trì xử lý bước này.

### Giữ tiến trình đã học

- Giữ ID câu/đề và thứ tự lựa chọn đã phát hành khi bổ sung nội dung.
- Không chèn/đảo dòng câu cũ trong tệp authored: ID hiện được cấp theo thứ tự trong từng chương.
- Khi sửa khóa chấm hoặc tập lựa chọn, mô tả ảnh hưởng tới câu trả lời đã lưu và cách chuyển dữ liệu trước khi phát hành.
- Câu trùng trong đề gốc vẫn giữ vị trí đề, gộp theo nội dung ở Toàn bộ; thứ tự A–D của từng bản có thể khác nhau.
- Câu nhiều đáp án hợp lý hoặc thiếu căn cứ cần ghi nhận để đối chiếu.

## 5. Dựng dữ liệu và kiểm tra

Chạy tại gốc repo, có Python và Node.js trong PATH. Dựng ảnh PDF cần `python -m pip install pymupdf pillow`. Xuất lại PowerPoint CNXHKH cần Windows có PowerPoint.

### CNXHKH

```sh
python build_data.py
python audit_questions.py
```

### HCM theo slide

```sh
python compile_hcm_bank.py
python build_hcm_data.py
python audit_hcm_data.py
```

Khi thay PDF hoặc tạo lại ảnh, chạy `python render_hcm_slides.py` trước khi dựng dữ liệu. `import_hcm_chapter3.py` dành riêng cho nguồn chương 3 hiện có, không phải bộ nhập chương bất kỳ.

### Ngân hàng HCM và đối chiếu

```sh
python build_hcm_bank.py
python audit_hcm_bank.py
python audit_hcm_slide_links.py
```

`import_hcm_bank.py` dành cho bản nguồn sáu tập hiện tại; chỉ chạy lại khi sửa nguồn đó. Nếu sửa nguồn slide dùng chung, dựng cả `build_hcm_data.py` và `build_hcm_bank.py`.

### Luồng học và kiểm tra thủ công

```sh
node --check dist/app.js
node --experimental-vm-modules tests/progress-smoke.mjs
python -m http.server 4173 -d dist
```

Mở http://localhost:4173, kiểm tra câu mới, đáp án, giải thích, ảnh đúng trang, làm lại và bộ lọc. Đổi ảnh/giao diện thì kèm ảnh kết quả trong PR. Khi thêm dữ liệu, cập nhật số lượng kiểm tra theo thực tế và giữ kiểm tra nguồn, câu trùng, tiến trình; không xóa kiểm tra để bỏ qua lỗi.

## 6. Trước khi gửi

- [ ] Có nguồn và trang kiểm tra được.
- [ ] Phân biệt câu gốc, tự soạn, phục dựng và phần chưa xác nhận.
- [ ] Giải thích đáp án, rà lựa chọn chồng lấn và câu trùng.
- [ ] Giữ ID/tiến trình hoặc mô tả cách chuyển dữ liệu.
- [ ] Nếu tích hợp: dựng đầu ra, chạy kiểm tra và xem trên localhost.

Có thể gửi đóng góp nhỏ, rõ nguồn để rà độc lập; không cần đợi đủ cả môn hoặc cả chương.
