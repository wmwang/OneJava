//B1題型-缺少套件引入
//問題：未引入 java.util.Scanner，導致無法識別 Scanner 類。


public class MissingImportExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // 錯誤：找不到符號 Scanner
        System.out.println("Enter a number:");
        int number = scanner.nextInt();
        System.out.println("You entered: " + number);
    }
}


//解決方式：添加 import java.util.Scanner;。