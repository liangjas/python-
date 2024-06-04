def print_multiplication_table():
    i = 1  # 外層迴圈
    while i < 10:
        j = 1  # 內層迴圈
        while j <= i:
            print(f"{j} x {i} = {i * j}", end='\t')
            j += 1  # 內層迴圈遞增
        print()  # 結束後換行
        i += 1  # 外層迴圈遞增

# 呼叫函數輸出乘法表
print_multiplication_table()