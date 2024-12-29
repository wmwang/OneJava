##====================================
##題目說明：f-string (Python 3.6+ 支援)
##問題：使用 f-string 格式化字串，但 f-string 在 Python 3.6 之前不被支援。
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

def greet(name):
    print(f"Hello, {name}!")  # 錯誤：舊版本不支援 f-string

greet("Alice")


#可能的錯誤訊息： SyntaxError: invalid syntax