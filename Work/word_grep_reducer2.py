
import sys

current_word = None
current_count = 0
word = None

# Danh sách các dòng chứa chuỗi mẫu
lines = set()
# Đọc các cặp key-value từ stdin
for line in sys.stdin:
    # Lấy key và value từ cặp key-value
    key, value = line.strip().split('\t', 1)
    lines.add(value)
    
for i in lines:
    print(i)
