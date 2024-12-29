//========================================================================
//題目說明：請協助將以下java 程式進行優化
//
//提示(題目組內部參考)：檢查每個數字是否為質數時，重複進行不必要的計算。
//
//題目Input： ./java/A3-2.java
//
//題目Output： 生成的檔案需為 ./java/A3-2-answer.py
//
//開發環境：
//請確認參賽包workshop_tool腳本已運行，將產生名為java-A3-2 container，可自動將./java/A3-2-answer.java程式在java21環境編譯並執行
//
//指令： docker run --rm -v ./java:/host-java-files java-A3-2
//
//驗證： 校驗腳本將分別對A3-2.java、A3-2-answer.java 兩個程式運行進行比對，確認.1)內存記憶體用量改善 or .2)執行時間改善。
//========================================================================

public class InefficientPrimeChecker {
    public static void main(String[] args) {
        int limit = 10000;
        for (int i = 2; i <= limit; i++) {
            if (isPrime(i)) {
                System.out.println(i + " is a prime number.");
            }
        }
    }

    public static boolean isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i < n; i++) { // 低效，未使用更好的演算法
            if (n % i == 0) return false;
        }
        return true;
    }
}
