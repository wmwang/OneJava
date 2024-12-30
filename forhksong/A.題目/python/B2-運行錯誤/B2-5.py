##B2題型- 遞歸過深（RecursionError）
##問題：遞歸沒有基礎情況，導致達到最大遞歸深度，觸發 RecursionError。
##
##驗證：
##請確認參賽包workshop_tool腳本已運行，其中python-3.x.x-app為已準備好的Python 3.x.x SDK runtime container，可執行下列指令獲得編譯結果
##
##>> docker run --rm -v $(pwd):/app python-3.x.x-app
def create_large_list():
    return [0] * (10**9)

if __name__ == "__main__":
    large_list = create_large_list()
    print("List created successfully")


##解決方式：為遞歸函數添加基礎情況來終止遞歸。