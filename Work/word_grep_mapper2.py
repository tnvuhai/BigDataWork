
import sys
pattern = sys.argv[1]

# Đọc dữ liệu đầu vào từ stdin và kiểm tra các dòng có chứa chuỗi mẫu
for line in sys.stdin:
    if pattern in line:
        # Ghi ra cặp key-value với key là chuỗi mẫu và value là dòng chứa chuỗi mẫu
        print('{0}\t{1}'.format(pattern, line.strip()))
