##====================================
##題目說明：以下程式在 Java 9 SDK可順利編譯，但Java 17 中會產生運行時的警告。
##
##題目要求：請透過LLM及相關tooling，調整程式，使得可以在Java17 環境中運行。
##
##驗證：
##請確認參賽包workshop_tool腳本已運行，其中python-3.x.x-app為已準備好的Python 3.x.x SDK runtime container，可執行下列指令獲得編譯結果
##
##>> docker run --rm -v $(pwd):/app python-3.x.x-app

##====================================
public class Main {
    @Override
    protected void finalize() throws Throwable {
        System.out.println("Finalize method called!");
    }

    public static void main(String[] args) {
        Main obj = new Main();
        obj = null;

        // 嘗試觸發垃圾回收
        System.gc();

        System.out.println("End of main method");
    }
}
