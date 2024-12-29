##B2題型-無窮迴圈（Infinite Loop）
##問題：使用錯誤的條件導致無窮迴圈。

def infinite_loop():
    while True:
        print("This will never stop")

if __name__ == "__main__":
    infinite_loop()



##解決方式：調整條件，讓迴圈在某個時刻停止。