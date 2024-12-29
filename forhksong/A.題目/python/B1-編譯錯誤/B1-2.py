##B1題型-未定義變數（NameError）
##問題：嘗試使用尚未定義的變數。


def calculate_area():
    return length * width

if __name__ == "__main__":
    print(calculate_area())


##預期解法：定義變數 length 和 width 並賦值，例如 length = 5; width = 10。