//========================================================================
//題目說明：請協助將解決java 程式編譯錯誤
//
//提示(題目組內部參考)：呼叫會拋出檢查型異常的方法時未處理異常。
//
//題目Input： ./java/B1-4.java
//
//題目Output： 生成的檔案需為 ./java/B1-4-answer.py
//
//開發環境：
//請確認參賽包workshop_tool腳本已運行，將產生名為java-B1-4 container，可自動將./java/B1-4-answer.java程式在java21環境編譯並執行
//
//指令： docker run --rm -v ./java:/host-java-files java-B1-4
//
//驗證： 校驗腳本將分別對B1-4.java、B1-4-answer.java 兩個程式運行進行比對，，確認.1)編譯結果正確及.2)程式輸出結果一致。
//========================================================================


import java.io.File;
import java.io.FileReader;

public class UnhandledExceptionExample {
    public static void main(String[] args) {
        File file = new File("example.txt");
        FileReader reader = new FileReader(file); // 錯誤：未處理的異常 FileNotFoundException
        System.out.println("File opened successfully.");
    }
}

//使用 try-catch 塊包裹操作，或在方法簽名上宣告 throws Exception。