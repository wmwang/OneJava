//B2題型-靜態與非靜態錯誤
//問題：從靜態方法中直接調用非靜態方法。

public class StaticVsNonStatic {
    public static void main(String[] args) {
        printMessage(); // 錯誤：非靜態方法無法從靜態上下文調用
    }

    public void printMessage() {
        System.out.println("This is a non-static method.");
    }
}

//解決方式：將方法 printMessage 改為靜態方法，或者通過創建物件來調用。
