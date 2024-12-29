//========================================================================
//題目說明：以下程式只能在較java 9+版本的SDK運行，請透過自動化工具調整為在較舊的SDK也可運行
//
//提示(題目組內部參考)：List.of 方法在 Java 9 之前不可用。
//
//題目Input： ./java/A1-4.java
//
//題目Output： 生成的檔案需為 ./java/A1-4-answer.java
//
//開發環境：
//請確認參賽包workshop_tool腳本已運行，將產生名為java-A1-4 container，可自動將./java/A1-4-answer.java程式在Java 17環境編譯並執行
//
//指令： docker run --rm -v ./java:/host-java-files java-A1-4 
//
//驗證： 校驗腳本將分別對A1-4.java、A1-4-answer.java 兩個程式輸出結果比對，確認.1)編譯結果正確及.2)程式輸出結果一致。
//========================================================================

import java.util.List;

public class ListExample {
    public static void main(String[] args) {
        List<String> fruits = List.of("Apple", "Banana", "Cherry");
        System.out.println(fruits);
    }
}

//預期解法：改用 Arrays.asList 或手動添加元素。