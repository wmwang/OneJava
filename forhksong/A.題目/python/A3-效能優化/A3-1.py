##A3題型: 不必要的重複計算
##效能問題：重複計算相同的子問題（可用動態規劃優化）。
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    n = 35
    print(f"Fibonacci({n}): {fibonacci(n)}")

