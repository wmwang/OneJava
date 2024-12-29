//========================================================================
//題目說明：請協助將以下java 程式轉換為Python
//
//提示(題目組內部參考)：集合操作 (計算不重複數字的總和)
//
//題目Input： ./java/A2-4.java
//
//題目Output： 生成的檔案需為 ./java/A2-4-answer.py
//
//開發環境：
//請確認參賽包workshop_tool腳本已運行，將產生名為java-A2-4 container，可自動將./java/A2-4-answer.py程式在python 3.x環境編譯並執行
//
//指令： docker run --rm -v ./java:/host-java-files java-A2-4
//
//驗證： 校驗腳本將分別對A2-4.java、A2-4-answer.py 兩個程式輸出結果比對，確認.1)編譯結果正確及.2)程式輸出結果一致。
//========================================================================

import java.io.*;
import java.util.Scanner;

public class FileHandler {
    public static void main(String[] args) {
        String filePath = "example.txt";
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter content to write to the file:");
        String content = scanner.nextLine();

        // Write to file
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {
            writer.write(content);
            System.out.println("Content written to file successfully.");
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
            return;
        }

        // Read from file
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            System.out.println("Reading content from file:");
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.err.println("Error reading from file: " + e.getMessage());
        }
    }
}
