##A2題形-數學計算與 NumPy
##功能：使用 NumPy 計算一個矩陣的轉置和行列式。

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

