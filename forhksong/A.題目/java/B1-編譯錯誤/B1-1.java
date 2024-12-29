//========================================================================
//題目說明：請協助將解決java 程式編譯錯誤
//
//提示(題目組內部參考)：未引入 java.util.Scanner，導致無法識別 Scanner 類。
//
//題目Input： ./java/B1-1.java
//
//題目Output： 生成的檔案需為 ./java/B1-1-answer.py
//
//開發環境：
//請確認參賽包workshop_tool腳本已運行，將產生名為java-B1-1 container，可自動將./java/B1-1-answer.java程式在java21環境編譯並執行
//
//指令： docker run --rm -v ./java:/host-java-files java-B1-1
//
//驗證： 校驗腳本將分別對B1-1.java、B1-1-answer.java 兩個程式運行進行比對，，確認.1)編譯結果正確及.2)程式輸出結果一致。
//========================================================================

public class MissingImportExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // 錯誤：找不到符號 Scanner
        System.out.println("Enter a number:");
        int number = scanner.nextInt();
        System.out.println("You entered: " + number);
    }
}


//解決方式：添加 import java.util.Scanner;。