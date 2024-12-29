##B2題型- 除以零錯誤（ZeroDivisionError）
##問題：執行除法運算時，除數為零。

def divide_numbers(a, b):
    return a / b

if __name__ == "__main__":
    result = divide_numbers(10, 0)
    print(f"Result: {result}")



##解決方式：在執行除法前，檢查除數是否為零，避免除以零錯誤。
