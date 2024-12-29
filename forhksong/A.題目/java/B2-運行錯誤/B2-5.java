//B2題型-死循環 (Infinite Loop)
//問題：無限迴圈導致程式無法正常終止。

public class InfiniteLoopExample {
    public static void main(String[] args) {
        int count = 0;
        while (count >= 0) { // 錯誤：無限迴圈
            System.out.println("Count: " + count);
            count++; // 數字會溢出到負數，導致永遠不會停止
        }
    }
}

//解決方式：確保循環條件能在某一時刻變為 false。
