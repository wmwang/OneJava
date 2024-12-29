//========================================================================
//題目說明：以下程式只能在較java 10+版本的SDK運行，請透過自動化工具調整為在較舊的SDK也可運行
//
//提示(題目組內部參考)：var 關鍵字在 Java 10 之前的版本中不被支持。
//
//題目Input： ./java/A1-2.java
//
//題目Output： 生成的檔案需為 ./java/A1-2-answer.java
//
//開發環境：
//請確認參賽包workshop_tool腳本已運行，將產生名為java-A1-2 container，可自動將./java/A1-2-answer.java程式在Java 17環境編譯並執行
//
//指令： docker run --rm -v ./java:/host-java-files java-A1-2 
//
//驗證： 校驗腳本將分別對A1-2.java、A1-2-answer.java 兩個程式輸出結果比對，確認.1)編譯結果正確及.2)程式輸出結果一致。
//========================================================================

public class VarExample {
    public static void main(String[] args) {
        var message = "Hello, Java!";
        System.out.println(message);
    }
}



//預期解法：明確指定變數類型，例如將 var 替換為 String。