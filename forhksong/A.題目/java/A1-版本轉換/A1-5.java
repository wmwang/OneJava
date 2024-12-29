//====================================
//題目說明：以下程式在 Java 9 SDK可順利編譯，但Java 17 中會產生運行時的警告。
//
//題目要求：請透過LLM及相關tooling，調整程式，使得可以在Java17 環境中運行。
//
//驗證：
//請確認參賽包workshop_tool腳本已運行，其中java-17-app為已準備好的java 17 SDK runtime container，可執行下列指令獲得編譯結果
//
//>> docker run --rm -v $(pwd):/app java-17-app
//>> 會出現Exception in thread "main" java.lang.reflect.InaccessibleObjectException

//內部參考：在 Java 7 中，反射可以輕鬆訪問私有字段，但在 Java 17 的模塊化系統中，這種行為受到了更多限制，會導致 IllegalAccessException。
//====================================
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