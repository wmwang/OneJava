//========================================================================
//題目說明：請協助將以下java 程式進行優化
//
//提示(題目組內部參考)：無效的資料結構選擇 (過度使用 List 查詢)
//
//題目Input： ./java/A3-3.java
//
//題目Output： 生成的檔案需為 ./java/A3-3-answer.py
//
//開發環境：
//請確認參賽包workshop_tool腳本已運行，將產生名為java-A3-3 container，可自動將./java/A3-3-answer.java程式在java21環境編譯並執行
//
//指令： docker run --rm -v ./java:/host-java-files java-A3-3
//
//驗證： 校驗腳本將分別對A3-3.java、A3-3-answer.java 兩個程式運行進行比對，確認.1)內存記憶體用量改善 or .2)執行時間改善。
//========================================================================
import java.util.ArrayList;

public class InefficientListUsage {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0; i < 10000; i++) {
            list.add(i);
        }

        int searchCount = 0;
        for (int i = 0; i < 10000; i++) {
            if (list.contains(i)) { // 低效，`contains` 是 O(n)
                searchCount++;
            }
        }

        System.out.println("Total matches: " + searchCount);
    }
}
