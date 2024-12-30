##A3題型: 不必要的重複計算
##效能問題：重複計算相同的子問題（可用動態規劃優化）。
##
##驗證：
##請確認參賽包workshop_tool腳本已運行，其中python-3.x.x-app為已準備好的Python 3.x.x SDK runtime container，可執行下列指令獲得編譯結果
##
##>> docker run --rm -v $(pwd):/app python-3.x.x-app
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    n = 35
    print(f"Fibonacci({n}): {fibonacci(n)}")

