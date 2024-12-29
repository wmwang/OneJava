//========================================================================
//題目說明：請協助將解決java 程式編譯錯誤
//
//提示(題目組內部參考)：從靜態方法中直接調用非靜態方法。
//
//題目Input： ./java/B1-5.java
//
//題目Output： 生成的檔案需為 ./java/B1-5-answer.py
//
//開發環境：
//請確認參賽包workshop_tool腳本已運行，將產生名為java-B1-5 container，可自動將./java/B1-5-answer.java程式在java21環境編譯並執行
//
//指令： docker run --rm -v ./java:/host-java-files java-B1-5
//
//驗證： 校驗腳本將分別對B1-5.java、B1-5-answer.java 兩個程式運行進行比對，，確認.1)編譯結果正確及.2)程式輸出結果一致。
//========================================================================
public class StaticVsNonStatic {
    public static void main(String[] args) {
        printMessage(); // 錯誤：非靜態方法無法從靜態上下文調用
    }

    public void printMessage() {
        System.out.println("This is a non-static method.");
    }
}

//解決方式：將方法 printMessage 改為靜態方法，或者通過創建物件來調用。
