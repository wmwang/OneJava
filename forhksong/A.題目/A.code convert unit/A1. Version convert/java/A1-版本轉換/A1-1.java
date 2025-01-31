//====================================
//題目說明：以下程式用了一個特殊的類，這個類在 Java 9 中是允許的行為，但在 Java 17 中已被移除或更改，從而導致在 Java 17 中運行會出錯。
//
//題目要求：請透過LLM及相關tooling，調整程式，使得可以在Java17 環境中運行。
//
//驗證：
//請確認參賽包workshop_tool腳本已運行，其中java-17-app為已準備好的java 17 SDK runtime container，可執行下列指令獲得編譯結果
//docker run --rm -v $(pwd):/app java-17-app
//
//內部參考：這段代碼使用了 javax.security.cert 包中的類，這些類在 Java 7 是存在的，但自 Java 9 起已被移除，因此在 Java 17 中無法找到相關類。

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
