##B1題型-缺少必要的模組（ModuleNotFoundError）
##問題：嘗試使用未安裝的第三方模組。
##
##驗證：
##請確認參賽包workshop_tool腳本已運行，其中python-3.x.x-app為已準備好的Python 3.x.x SDK runtime container，可執行下列指令獲得編譯結果
##
##>> docker run --rm -v $(pwd):/app python-3.x.x-app
import numpy as np

def main():
    arr = np.array([1, 2, 3])
    print("Array:", arr)

if __name__ == "__main__":
    main()

##解決方式：運行 pip install numpy 來安裝模組，或檢查 Python 環境。
