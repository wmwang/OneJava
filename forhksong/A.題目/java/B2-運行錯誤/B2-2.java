//B2題型-數組越界 (ArrayIndexOutOfBoundsException)
//問題：訪問數組中不存在的索引。

public class ArrayIndexOutOfBoundsExample {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3};
        System.out.println("Number at index 3: " + numbers[3]); // 錯誤：ArrayIndexOutOfBoundsException
    }
}


//解決方式：檢查索引是否在數組範圍內。
