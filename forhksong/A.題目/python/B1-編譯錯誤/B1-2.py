##B1題型-未定義變數（NameError）
##問題：嘗試使用尚未定義的變數。
##
##驗證：
##請確認參賽包workshop_tool腳本已運行，其中python-3.x.x-app為已準備好的Python 3.x.x SDK runtime container，可執行下列指令獲得編譯結果
##
##>> docker run --rm -v $(pwd):/app python-3.x.x-app


def calculate_area():
    return length * width

if __name__ == "__main__":
    print(calculate_area())


##預期解法：定義變數 length 和 width 並賦值，例如 length = 5; width = 10。