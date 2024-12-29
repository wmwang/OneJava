##B1題型-語法錯誤（SyntaxError）
##問題：漏掉冒號，導致語法錯誤。


def greet(name)
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("Alice")


##預期解法：在 def greet(name) 後面添加冒號。