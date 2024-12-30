##A3題型: 不必要的內存使用
##效能問題：將文件的所有行讀入列表中並進行處理，即使文件很大，導致內存使用過多。
##
##驗證：
##請確認參賽包workshop_tool腳本已運行，其中python-3.x.x-app為已準備好的Python 3.x.x SDK runtime container，可執行下列指令獲得編譯結果
##
##>> docker run --rm -v $(pwd):/app python-3.x.x-app
def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()  # 整個文件一次性讀入內存
    return [line.strip() for line in lines]

if __name__ == "__main__":
    file_path = "large_file.txt"
    processed_lines = process_file(file_path)
    print(f"Processed {len(processed_lines)} lines.")




