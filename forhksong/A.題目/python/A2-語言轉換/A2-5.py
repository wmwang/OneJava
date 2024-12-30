##A2題形-數學計算與 NumPy
##功能：使用 NumPy 計算一個矩陣的轉置和行列式。、##
##驗證：
##請確認參賽包workshop_tool腳本已運行，其中python-3.x.x-app為已準備好的Python 3.x.x SDK runtime container，可執行下列指令獲得編譯結果
##
##>> docker run --rm -v $(pwd):/app python-3.x.x-app

import numpy as np

def matrix_operations(matrix):
    transpose = np.transpose(matrix)
    determinant = np.linalg.det(matrix)
    return transpose, determinant

if __name__ == "__main__":
    matrix = np.array([[1, 2], [3, 4]])
    transpose, determinant = matrix_operations(matrix)
    print("Original matrix:\n", matrix)
    print("Transpose:\n", transpose)
    print("Determinant:", determinant)

