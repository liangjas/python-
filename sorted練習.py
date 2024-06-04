my_list = [4, 3, 1, 1, 2, 7, 3, 7, 7, 3, 9]
sorted_list = sorted(my_list)
print(sorted_list)  # 輸出: [1, 1, 2, 3, 3, 3, 4, 7, 7, 7, 9]
#sorted  Python 的函數，用於返回一個排序後的列表。不會改變原來序列，而是生成一個新的已排序的列表。
#sorted 函數還可以接受幾個關鍵字參數來自定義排序行為：

#key函數，將被應用於每個元素進行排序。
#reverse如果為 True，則列表元素將被按降序排序
# 按字符串長度排序，並按降序排列
words = ["jason", "jake", "judy", "alice"]
sorted_words = sorted(words, key=len, reverse=True)
print(sorted_words)  # 輸出: ['jason', 'alice', 'jake', 'judy']