//B2題型-類型轉換異常 (ClassCastException)
//問題：嘗試將物件轉換為不兼容的類型。

public class ClassCastExceptionExample {
    public static void main(String[] args) {
        Object obj = "This is a string";
        Integer number = (Integer) obj; // 錯誤：ClassCastException
        System.out.println("Number: " + number);
    }
}



//解決方式：使用 instanceof 驗證物件的類型，避免不合法的類型轉換。
