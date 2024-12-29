##B1題型-模組匯入錯誤（ImportError）
##問題：匯入了一個不存在的模組。


import non_existing_module

def main():
    print("This will not run.")

if __name__ == "__main__":
    main()



##預期解法：確保匯入正確的模組名稱，或檢查是否需要安裝相關套件。