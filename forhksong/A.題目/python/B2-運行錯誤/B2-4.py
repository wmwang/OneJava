##B2題型-資料結構操作錯誤（IndexError）
##問題：嘗試訪問超出範圍的列表元素。

def access_element(lst, index):
    return lst[index]

if __name__ == "__main__":
    my_list = [1, 2, 3]
    print(access_element(my_list, 5))


##解決方式：檢查索引是否有效，避免訪問超出範圍的元素。