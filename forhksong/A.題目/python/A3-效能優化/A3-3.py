##A3題型: 非必要的嵌套迴圈
##效能問題：嵌套迴圈導致 $O(n^2)$ 的時間複雜度（可用哈希表優化）。
##
##驗證：
##請確認參賽包workshop_tool腳本已運行，其中python-3.x.x-app為已準備好的Python 3.x.x SDK runtime container，可執行下列指令獲得編譯結果
##
##>> docker run --rm -v $(pwd):/app python-3.x.x-app


def find_pairs(nums, target):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append((nums[i], nums[j]))
    return result

if __name__ == "__main__":
    nums = list(range(1, 1001))  # 大量數據
    target = 1000
    pairs = find_pairs(nums, target)
    print(f"Found {len(pairs)} pairs.")

