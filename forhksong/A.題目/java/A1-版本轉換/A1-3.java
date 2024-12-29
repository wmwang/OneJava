//========================================================================
//題目說明：以下程式只能在較舊版本的SDK運行，請透過自動化工具調整為在較新的SDK也可運行
//
//提示(題目組內部參考)：Thread.stop() 是早期java使用的函數，在較新的Java runtime環境會產生運行時的警告
//
//題目Input： ./java/A1-3.java
//
//題目Output： 生成的檔案需為 ./java/A1-3-answer.java
//
//開發環境：
//請確認參賽包workshop_tool腳本已運行，將產生名為java-A1-3 container，可自動將./java/A1-3-answer.java程式在Java 17環境編譯並執行
//
//指令： docker run --rm -v ./java:/host-java-files java-A1-3 
//
//驗證： 校驗腳本將分別對A1-3.java、A1-3-answer.java 兩個程式輸出結果比對，確認.1)編譯結果正確及.2)程式輸出結果一致。
//========================================================================

public class Main {
    public static void main(String[] args) {
        Thread thread = new Thread(() -> {
            while (true) {
                System.out.println("Running...");
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
        });

        thread.start();

        try {
            Thread.sleep(3000);
            // 強制停止線程
            thread.stop();
            System.out.println("Thread stopped");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
