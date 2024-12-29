//B1題型-方法簽名不匹配
//問題：方法參數的類型與調用時提供的不匹配。


public class MethodSignatureMismatch {
    public static void main(String[] args) {
        greet(42); // 錯誤：找不到符合的 greet 方法
    }

    public static void greet(String name) {
        System.out.println("Hello, " + name);
    }
}

//解決方式：新增方法 public static void greet(int number) 或調整參數為字串。
