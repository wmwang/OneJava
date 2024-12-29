##B2題型-記憶體不足（MemoryError）
##問題：創建一個非常大的列表，超出可用內存。

def create_large_list():
    return [0] * (10**9)

if __name__ == "__main__":
    large_list = create_large_list()
    print("List created successfully")


##解決方式：優化資料結構或限制數據大小，可以考慮使用生成器或其他方法減少內存占用。
