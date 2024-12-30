##====================================
##題目說明：dataclasses 模組 (Python 3.7+ 支援)
##問題：使用 dataclasses 模組定義資料類型，但該模組在 Python 3.7 之前不存在。
##
##題目要求：請透過LLM及相關tooling，調整程式，使得可以在Java17 環境中運行。
##
##驗證：
##請確認參賽包workshop_tool腳本已運行，其中python-3.x.x-app為已準備好的Python 3.x.x SDK runtime container，可執行下列指令獲得編譯結果
##
##>> docker run --rm -v $(pwd):/app python-3.x.x-app
##====================================

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

person = Person(name="Alice", age=30)
print(person)  # 錯誤：舊版本不支援 dataclasses 模組



#可能的錯誤訊息： ModuleNotFoundError: No module named 'dataclasses'
#解決方式：在低版本中安裝 dataclasses backport，或手動實現類似的類別結構。