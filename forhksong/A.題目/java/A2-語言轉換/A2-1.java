//========================================================================
//題目說明：請協助將以下java 程式轉換為Python
//
//提示(題目組內部參考)：遞迴計算階乘 + 簡單輸入
//
//題目Input： ./java/A2-1.java
//
//題目Output： 生成的檔案需為 ./java/A2-1-answer.py
//
//開發環境：
//請確認參賽包workshop_tool腳本已運行，將產生名為java-A2-1 container，可自動將./java/A2-1-answer.py程式在python 3.x環境編譯並執行
//
//指令： docker run --rm -v ./java:/host-java-files java-A2-1
//
//驗證： 校驗腳本將分別對A2-1.java、A2-1-answer.py 兩個程式輸出結果比對，確認.1)編譯結果正確及.2)程式輸出結果一致。
//========================================================================

import java.util.Scanner;

public class FactorialCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number to calculate its factorial: ");
        
        if (!scanner.hasNextInt()) {
            System.out.println("Invalid input. Please enter an integer.");
            return;
        }

        int number = scanner.nextInt();
        if (number < 0) {
            System.out.println("Factorial is not defined for negative numbers.");
        } else {
            int result = factorial(number);
            System.out.println("Factorial of " + number + " is " + result);
        }
    }

    public static int factorial(int n) {
        if (n == 0) {
            return 1;
        }
        return n * factorial(n - 1);
    }
}
