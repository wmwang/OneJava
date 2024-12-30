##B1題型-語法錯誤（SyntaxError）
##問題：漏掉冒號，導致語法錯誤。
##
##驗證：
##請確認參賽包workshop_tool腳本已運行，其中python-3.x.x-app為已準備好的Python 3.x.x SDK runtime container，可執行下列指令獲得編譯結果
##
##>> docker run --rm -v $(pwd):/app python-3.x.x-app


def greet(name)
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("Alice")


##預期解法：在 def greet(name) 後面添加冒號。