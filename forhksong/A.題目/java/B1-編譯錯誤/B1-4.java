//B1題型-未處理的異常
//問題：呼叫會拋出檢查型異常的方法時未處理異常。


import java.io.File;
import java.io.FileReader;

public class UnhandledExceptionExample {
    public static void main(String[] args) {
        File file = new File("example.txt");
        FileReader reader = new FileReader(file); // 錯誤：未處理的異常 FileNotFoundException
        System.out.println("File opened successfully.");
    }
}

//使用 try-catch 塊包裹操作，或在方法簽名上宣告 throws Exception。