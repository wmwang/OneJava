//========================================================================
//題目說明：以下程式只能在較舊版本的SDK運行，請透過自動化工具調整為在較新的SDK也可運行
//
//提示(題目組內部參考)：在 Java 7 中，反射可以輕鬆訪問私有字段，但在 Java 17 的模塊化系統中，這種行為受到了更多限制，會導致 IllegalAccessException。
//
//題目Input： ./java/A1-5.java
//
//題目Output： 生成的檔案需為 ./java/A1-5-answer.java
//驗證：
//請確認參賽包workshop_tool腳本已運行，其中java-17-app為已準備好的java 17 SDK runtime container，可執行下列指令獲得編譯結果
//
//開發環境：
//請確認參賽包workshop_tool腳本已運行，將產生名為java-A1-5 container，可自動將./java/A1-4-answer.java程式在Java 17環境編譯並執行
//
//指令： docker run --rm -v ./java:/host-java-files java-A1-5
//
//驗證： 校驗腳本將分別對A1-5.java、A1-5-answer.java 兩個程式輸出結果比對，確認.1)編譯結果正確及.2)程式輸出結果一致。
//========================================================================

import java.lang.reflect.Field;

public class Main {
    private String secret = "This is a secret";

    public static void main(String[] args) {
        try {
            Main obj = new Main();
            Field field = Main.class.getDeclaredField("secret");
            field.setAccessible(true); // 強制設置可訪問
            String value = (String) field.get(obj);
            System.out.println("Secret value: " + value);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}