//========================================================================
//題目說明：請協助將以下java 程式進行優化
//
//提示(題目組內部參考)：重複排序操作
//
//題目Input： ./java/A3-5.java
//
//題目Output： 生成的檔案需為 ./java/A3-5-answer.py
//
//開發環境：
//請確認參賽包workshop_tool腳本已運行，將產生名為java-A3-5 container，可自動將./java/A3-5-answer.java程式在java21環境編譯並執行
//
//指令： docker run --rm -v ./java:/host-java-files java-A3-5
//
//驗證： 校驗腳本將分別對A3-5.java、A3-5-answer.java 兩個程式運行進行比對，確認.1)內存記憶體用量改善 or .2)執行時間改善。
//========================================================================
import java.util.ArrayList;
import java.util.Collections;

public class InefficientSorting {
    public static void main(String[] args) {
        ArrayList<Integer> numbers = new ArrayList<>();

        for (int i = 0; i < 10000; i++) {
            numbers.add((int) (Math.random() * 10000));
            Collections.sort(numbers); // 每次插入後都排序，低效
        }

        System.out.println("First 10 sorted numbers: " + numbers.subList(0, 10));
    }
}
