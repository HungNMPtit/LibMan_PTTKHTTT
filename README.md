# Chủ đề: Hệ thống quản lý thư viện đại học <LibMan>

## Bài tập lớn cuối kỳ môn Phân tích thiết kế hệ thống thông tin - PTIT

## Mô tả bài tập:

Hệ thống quản lý Thư viện (LibMan) của một trường Đại học cho phép quản lý các loại tài liệu thông thường (sách, giáo trình, tạp chí…). Chức năng, nhiệm vụ của từng đối tượng như sau:
- Nhân viên quản lí - xem dạng báo cáo thống kê: tài liệu theo số lần mượn, độc giả theo số lần mượn, nhà cung cấp theo số lượng tài liệu nhập.
- Nhân viên thư viện: Cập nhật tài liệu, bạn đọc, nhà cung cấp (thêm, xóa, thay đổi), tìm kiếm, cho mượn tài liệu, nhận trả tài liệu từ bạn đọc, nhập tài liệu từ nhà cung cấp. 
- Bạn đọc: mượn tài liệu, trả tài liệu trực tiếp với nhân viên, tìm kiếm thông tin tài liệu, đăng kí làm thẻ bạn đọc trực tuyến. 

#### Module chức năng
1. Tìm thông tin tài liệu
    - Bước 1: Chọn menu tìm tài liệu 
    - Bước 2: Nhập tên tài liệu để tìm 
    - Bước 3: Hệ thống hiện danh sách các tài liệu có tên chứa từ khóa vừa nhập 
    - Bước 4: Click vào một tài liệu xem chi tiết 
    - Bước 5: Hệ thống hiện thông tin chi tiết về tài liệu.

 
2. Cho bạn đọc mượn tài liệu
    - Bước 1: Chọn menu cho mượn tài liệu
    - Bước 2: Quét thẻ độc giả (hoặc tìm kiếm theo mã)
    - Bước 3: Lặp các bước sau cho hết tài liệu mượn: quét mã tài liệu (hoặc tìm theo mã)
    - Bước 4: Lặp đến khi hết các tài liệu mượn vào thì submit
    - Bước 5: In phiếu mượn và giao cho độc giả

3. Đăng kí làm thẻ bạn đọc
    - Bước 1: Chọn menu đăng kí làm thẻ bạn đọc
    - Bước 2: Nhập thông tin bạn đọc và thẻ, click thêm
    - Bước 3: Hệ thống báo thành công

4. Tìm thông tin tài liệu
    - Bước 1: Chọn menu tìm tài liệu 
    - Bước 2: Nhập tên tài liệu để tìm
    - Bước 3: Hệ thống hiện danh sách các tài liệu có tên chứa từ khóa vừa nhập 
    - Bước 4: Click vào một tài liệu xem chi tiết
    - Bước 5: Hệ thống hiện thông tin chi tiết về tài liệu.

5. Nhập tài liệu từ nhà cung cấp
    - Bước 1: Chọn menu nhập tài liệu
    - Bước 2: Tìm nhà cung cấp theo tên (thêm mới nếu chưa có)
    - Bước 3: Lặp các bước sau cho hết tài liệu nhập: quét mã tài liệu (hoặc tìm theo mã, thêm mới nếu chưa có)
    - Bước 4: Nhập số lượng và đơn giá
    - Bước 5: Lặp đến khi hết các tài liệu nhập vào thì submit 
    - Bước 6: In hóa đơn và thanh toán cho nhà cung cấp

6. Thống kê tài liệu theo số lần mượn
    - Bước 1: Chọn menu xem báo cáo 
    - Bước 2: Chọn thống kê tài liệu theo lượt mượn 
    - Bước 3: Chọn ngày bắt đầu, kết thúc thống kê 
    - Bước 4: Xem thống kê tài liệu 
    - Bước 5: Click vào một tài liệu 
    - Bước 6: Xem chi tiết các lần tài liệu được mượn 
    - Bước 7: Click một lần mượn 
    - Bước 8: Xem chi tiết phiếu mượn tương ứng

7. Xem thống kê độc giả theo số lần mượn
    - Bước 1: Chọn menu xem báo cáo 
    - Bước 2: Chọn xem thống kê độc giả theo lượt mượn 
    - Bước 3: Chọn ngày bắt đầu, kết thúc thống kê 
    - Bước 4: Xem thống kê độc giả 
    - Bước 5: Click vào một độc giả 
    - Bước 6: Xem chi tiết các lần độc giả mượn 
    - Bước 7: Click một lần mượn 
    - Bước 8: Xem chi tiết phiếu mượn tương ứng

8. Xem thống kê nhà cung cấp theo số lượng nhập
    - Bước 1: Chọn menu xem báo cáo
    - Bước 2: Chọn xem thống kê nhà cung cấp theo lượng nhập
    - Bước 3: Chọn ngày bắt đầu, kết thúc thống kê
    - Bước 4: Xem thống kê nhà cung cấp
    - Bước 5: Click vào một nhà cung cấp
    - Bước 6: Xem chi tiết các lần nhập tài liệu
    - Bước 7: Click một lần nhập
    - Bước 8: Xem chi tiết hóa đơn nhập tương ứng