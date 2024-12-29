##A2題形-字符串處理與列表操作
##功能：讀取一個字符串，分割為單詞列表，過濾掉短於 3 個字符的單詞，並按長度排序。

def process_text(input_text):
    words = input_text.split()
    filtered_words = [word for word in words if len(word) >= 3]
    sorted_words = sorted(filtered_words, key=len)
    return sorted_words

if __name__ == "__main__":
    text = "This is an example of text processing in Python"
    result = process_text(text)
    print("Processed words:", result)
