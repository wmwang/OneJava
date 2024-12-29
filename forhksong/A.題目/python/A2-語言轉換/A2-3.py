##A2題形-字典操作與文件處理
##功能：讀取一個文本文件，計算每個單詞出現的次數，並以字典形式返回。

def word_count(file_path):
    word_freq = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

if __name__ == "__main__":
    file_path = "example.txt"
    word_frequencies = word_count(file_path)
    print("Word frequencies:", word_frequencies)
