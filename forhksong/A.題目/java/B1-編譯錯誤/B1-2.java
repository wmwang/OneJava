//========================================================================
//題目說明：請協助將解決java 程式編譯錯誤
//
//提示(題目組內部參考)：方法參數的類型與調用時提供的不匹配。
//
//題目Input： ./java/B1-2.java
//
//題目Output： 生成的檔案需為 ./java/B1-2-answer.py
//
//開發環境：
//請確認參賽包workshop_tool腳本已運行，將產生名為java-B1-2 container，可自動將./java/B1-2-answer.java程式在java21環境編譯並執行
//
//指令： docker run --rm -v ./java:/host-java-files java-B1-2
//
//驗證： 校驗腳本將分別對B1-2.java、B1-2-answer.java 兩個程式運行進行比對，，確認.1)編譯結果正確及.2)程式輸出結果一致。
//========================================================================

public class MethodSignatureMismatch {
    public static void main(String[] args) {
        greet(42); // 錯誤：找不到符合的 greet 方法
    }

    public static void greet(String name) {
        System.out.println("Hello, " + name);
    }
}

//解決方式：新增方法 public static void greet(int number) 或調整參數為字串。
