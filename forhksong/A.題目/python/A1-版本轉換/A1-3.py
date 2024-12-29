##====================================
##題目說明：typing 模組 (Python 3.5+ 支援)
##問題：使用 typing 模組進行類型註解，該模組在 Python 3.5 之前不存在。
##
##題目要求：請透過LLM及相關tooling，調整程式，使得可以在Java17 環境中運行。
##
##驗證：
##請確認參賽包workshop_tool腳本已運行，其中java-17-app為已準備好的java 17 SDK runtime container，可執行下列指令獲得編譯結果
##
##>> docker run --rm -v $(pwd):/app java-17-app
##>> 會出現Exception in thread "main" java.lang.reflect.InaccessibleObjectException

##內部參考：在 Java 7 中，反射可以輕鬆訪問私有字段，但在 Java 17 的模塊化系統中，這種行為受到了更多限制，會導致 IllegalAccessException。
##====================================

from typing import List

def add_numbers(numbers: List[int]) -> int:
    return sum(numbers)

print(add_numbers([1, 2, 3]))  # 錯誤：舊版本不支援 typing 模組



#可能的錯誤訊息： ImportError: No module named typing