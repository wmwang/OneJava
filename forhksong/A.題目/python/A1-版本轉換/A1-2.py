##====================================
##題目說明：async 和 await 關鍵字 (Python 3.5+ 支援)
##問題：async 和 await 關鍵字在 Python 3.5 之前不被支援。
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

import asyncio

async def main():
    print("Hello, Async!")

asyncio.run(main())  # 錯誤：舊版本不支援 async/await 語法


#可能的錯誤訊息： SyntaxError: invalid syntax