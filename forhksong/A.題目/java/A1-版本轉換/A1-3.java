//====================================
//題目說明：以下程式在 Java 9 SDK可順利編譯，但Java 17 中會產生運行時的警告。
//
//題目要求：請透過LLM及相關tooling，調整程式，使得可以在Java17 環境中運行。
//
//驗證：
//請確認參賽包workshop_tool腳本已運行，其中java-17-app為已準備好的java 17 SDK runtime container，可執行下列指令獲得編譯結果
//
//>> docker run --rm -v $(pwd):/app java-17-app
//>> 會出現WARNING: Thread.stop() is inherently unsafe and may cause inconsistent state
//
//內部參考：Thread.stop() 是早起java使用的函數，在較新的Java runtime環境會產生運行時的警告
//====================================
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
