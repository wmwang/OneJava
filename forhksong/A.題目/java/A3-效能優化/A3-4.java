//========================================================================
//題目說明：請協助將以下java 程式進行優化
//
//提示(題目組內部參考)：過度的物件創建
//
//題目Input： ./java/A3-4.java
//
//題目Output： 生成的檔案需為 ./java/A3-4-answer.py
//
//開發環境：
//請確認參賽包workshop_tool腳本已運行，將產生名為java-A3-4 container，可自動將./java/A3-4-answer.java程式在java21環境編譯並執行
//
//指令： docker run --rm -v ./java:/host-java-files java-A3-4
//
//驗證： 校驗腳本將分別對A3-4.java、A3-4-answer.java 兩個程式運行進行比對，確認.1)內存記憶體用量改善 or .2)執行時間改善。
//========================================================================
import java.util.ArrayList;

public class ExcessiveObjectCreation {
    public static void main(String[] args) {
        for (int i = 0; i < 10000; i++) {
            MyObject obj = new MyObject("Object " + i); // 每次都創建新物件
            obj.printName();
        }
    }
}

class MyObject {
    private String name;

    public MyObject(String name) {
        this.name = name;
    }

    public void printName() {
        System.out.println(name);
    }
}

