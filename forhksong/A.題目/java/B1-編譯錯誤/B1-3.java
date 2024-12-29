//B1題型-類別名稱拼錯
//問題：問題：程式中引用的類別名稱與定義的名稱不一致。


public class TypoInClassName {
    public static void main(String[] args) {
        MyCalulator calculator = new MyCalculator(); // 錯誤：找不到符號 MyCalulator
        System.out.println("Result: " + calculator.add(5, 10));
    }
}

class MyCalculator {
    public int add(int a, int b) {
        return a + b;
    }
}

//解決方式：修正變數型別名稱為正確的 MyCalculator。