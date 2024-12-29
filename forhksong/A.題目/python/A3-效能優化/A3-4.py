##A3題型: 使用了低效的數據結構
##效能問題：內部列表搜索操作效率低，可用字典優化。
def count_frequencies(nums):
    freq = []
    for num in nums:
        found = False
        for i in range(len(freq)):
            if freq[i][0] == num:
                freq[i] = (num, freq[i][1] + 1)
                found = True
                break
        if not found:
            freq.append((num, 1))
    return freq

if __name__ == "__main__":
    nums = [1, 2, 3, 1, 2, 1] * 1000  # 大量數據
    frequencies = count_frequencies(nums)
    print(frequencies[:10])
