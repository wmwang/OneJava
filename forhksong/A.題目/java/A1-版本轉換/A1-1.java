//========================================================================
//題目說明：以下程式只能在較舊版本的SDK運行，請透過自動化工具調整為在較新的SDK也可運行
//
//提示(題目組內部參考)：以下程式用了一個特殊的類，這個類在 Java 9 中是允許的行為，但在 Java 17 中已被移除或更改，從而導致在 Java 17 中運行會出錯。
//
//題目Input： ./java/A1-1.java
//
//題目Output： 生成的檔案需為 ./java/A1-1-answer.java
//
//開發環境：
//請確認參賽包workshop_tool腳本已運行，將產生名為java-A1-1 container，可自動將./java/A1-1-answer.java程式在Java 17環境編譯並執行
//
//指令： docker run --rm -v ./java:/host-java-files java-A1-1 
//
//驗證： 校驗腳本將分別對A1-1.java、A1-1-answer.java 兩個程式輸出結果比對，確認.1)編譯結果正確及.2)程式輸出結果一致。
//========================================================================



import javax.security.cert.X509Certificate;

public class A1-1 {
    public static void main(String[] args) {
        try {
            X509Certificate cert = X509Certificate.getInstance(new byte[0]);
            System.out.println("Certificate: " + cert);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
