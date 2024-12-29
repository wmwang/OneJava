//========================================================================
//題目說明：請協助將以下java 程式轉換為Python
//
//提示(題目組內部參考)：集合操作 (計算不重複數字的總和)
//
//題目Input： ./java/A2-3.java
//
//題目Output： 生成的檔案需為 ./java/A2-3-answer.py
//
//開發環境：
//請確認參賽包workshop_tool腳本已運行，將產生名為java-A2-3 container，可自動將./java/A2-3-answer.py程式在python 3.x環境編譯並執行
//
//指令： docker run --rm -v ./java:/host-java-files java-A2-3
//
//驗證： 校驗腳本將分別對A2-3.java、A2-3-answer.py 兩個程式輸出結果比對，確認.1)編譯結果正確及.2)程式輸出結果一致。
//========================================================================

public class MatrixOperations {
    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        int rows = matrix.length;
        int cols = matrix[0].length;
        int[][] transposed = new int[cols][rows];

        System.out.println("Original Matrix:");
        printMatrix(matrix);

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                transposed[j][i] = matrix[i][j];
            }
        }

        System.out.println("Transposed Matrix:");
        printMatrix(transposed);

        int diagonalSum = calculateDiagonalSum(transposed);
        System.out.println("Sum of diagonal elements in transposed matrix: " + diagonalSum);
    }

    public static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            for (int val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
    }

    public static int calculateDiagonalSum(int[][] matrix) {
        int sum = 0;
        for (int i = 0; i < matrix.length; i++) {
            sum += matrix[i][i];
        }
        return sum;
    }
}

