##====================================
##題目說明：Dictionary Comprehension 的排序保證 (Python 3.7+ 支援)
##問題：使用 typing 模組進行類型註解，該模組在 Python 3.7 之前不存在。
##
##題目要求：請透過LLM及相關tooling，調整程式，使得可以在Java17 環境中運行。
##
##驗證：
##請確認參賽包workshop_tool腳本已運行，其中python-3.x.x-app為已準備好的Python 3.x.x SDK runtime container，可執行下列指令獲得編譯結果
##
##>> docker run --rm -v $(pwd):/app python-3.x.x-app
##====================================
data = {i: chr(65 + i) for i in range(5)}
print(data)  # 錯誤：舊版本字典可能不保證有序


##可能的問題行為： 輸出的字典順序不一致，可能導致後續程式邏輯錯誤。
