

# Viết mã để thêm dấu - vào đầu dòng với input là cả văn bản
# Bước 1: Chọn menu xem báo cáo 
# Bước 2: Chọn xem thống kê nhà cung cấp theo lượng nhập 
# Bước 3: Chọn ngày bắt đầu, kết thúc thống kê
# Bước 4: Xem thống kê nhà cung cấp 
# Bước 5: Click vào một nhà cung cấp 
# Bước 6: Xem chi tiết các lần nhập tài liệu 
# Bước 7: Click một lần nhập 
# Bước 8: Xem chi tiết hóa đơn nhập tương ứng

def add_dash_to_line(text):
    lines = text.split('\n')
    result = ''
    for line in lines:
        result += '- ' + line + '\n'
    return result

text = '''
Bước 1: Chọn menu xem báo cáo 
Bước 2: Chọn xem thống kê nhà cung cấp theo lượng nhập 
Bước 3: Chọn ngày bắt đầu, kết thúc thống kê
Bước 4: Xem thống kê nhà cung cấp 
Bước 5: Click vào một nhà cung cấp 
Bước 6: Xem chi tiết các lần nhập tài liệu 
Bước 7: Click một lần nhập 
Bước 8: Xem chi tiết hóa đơn nhập tương ứng
'''

print(add_dash_to_line(text))