def print_hexagon(size):
    # 打印上半
    for i in range(size):
        print(' ' * (size - i - 1) + '* ' * (size + i))
#切一半
    # 打印下半
    for i in range(size - 1, -1, -1):
        print(' ' * (size - i - 1) + '* ' * (size + i))

# 設置六邊形大小
hexagon_size = 8
print_hexagon(hexagon_size)