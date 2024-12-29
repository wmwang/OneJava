##B1題型-缺少必要的模組（ModuleNotFoundError）
##問題：嘗試使用未安裝的第三方模組。

import numpy as np

def main():
    arr = np.array([1, 2, 3])
    print("Array:", arr)

if __name__ == "__main__":
    main()

##解決方式：運行 pip install numpy 來安裝模組，或檢查 Python 環境。
