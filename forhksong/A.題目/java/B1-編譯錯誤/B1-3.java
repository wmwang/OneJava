//========================================================================
//題目說明：請協助將解決java 程式編譯錯誤
//
//提示(題目組內部參考)：程式中引用的類別名稱與定義的名稱不一致。
//
//題目Input： ./java/B1-3.java
//
//題目Output： 生成的檔案需為 ./java/B1-3-answer.py
//
//開發環境：
//請確認參賽包workshop_tool腳本已運行，將產生名為java-B1-3 container，可自動將./java/B1-3-answer.java程式在java21環境編譯並執行
//
//指令： docker run --rm -v ./java:/host-java-files java-B1-3
//
//驗證： 校驗腳本將分別對B1-3.java、B1-3-answer.java 兩個程式運行進行比對，，確認.1)編譯結果正確及.2)程式輸出結果一致。
//========================================================================


public class TypoInClassName {
    public static void main(String[] args) {
        MyCalulator calculator = new MyCalculator(); // 錯誤：找不到符號 MyCalulator
        System.out.println("Result: " + calculator.add(5, 10));
    }
}

class MyCalculator {
    public int add(int a, int b) {
        return a + b;
    }
}

//解決方式：修正變數型別名稱為正確的 MyCalculator。