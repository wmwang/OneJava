//B2題型-空指針異常 (NullPointerException)
//問題：嘗試在空物件上調用方法。

public class NullPointerExample {
    public static void main(String[] args) {
        String str = null;
        System.out.println("Length of string: " + str.length()); // 錯誤：NullPointerException
    }
}

//解決方式：在使用物件前檢查是否為 null。
