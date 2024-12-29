//========================================================================
//題目說明：請協助將以下java 程式轉換為Python
//
//提示(題目組內部參考)：集合操作 (計算不重複數字的總和)
//
//題目Input： ./java/A2-2.java
//
//題目Output： 生成的檔案需為 ./java/A2-2-answer.py
//
//開發環境：
//請確認參賽包workshop_tool腳本已運行，將產生名為java-A2-2 container，可自動將./java/A2-2-answer.py程式在python 3.x環境編譯並執行
//
//指令： docker run --rm -v ./java:/host-java-files java-A2-2
//
//驗證： 校驗腳本將分別對A2-2.java、A2-2-answer.py 兩個程式輸出結果比對，確認.1)編譯結果正確及.2)程式輸出結果一致。
//========================================================================

import java.util.HashSet;

public class UniqueNumbers {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 2, 3, 4, 4, 5, 6, 6, 7};
        HashSet<Integer> uniqueNumbers = new HashSet<>();
        int sum = 0;

        for (int num : numbers) {
            if (uniqueNumbers.add(num)) {
                sum += num;
            }
        }

        System.out.println("Unique Numbers: " + uniqueNumbers);
        System.out.println("Sum of unique numbers: " + sum);

        System.out.println("Iterating through unique numbers:");
        for (int unique : uniqueNumbers) {
            System.out.println("- " + unique);
        }
    }
}

