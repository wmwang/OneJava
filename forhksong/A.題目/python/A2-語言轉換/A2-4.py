##A2題形-類與繼承
##功能：定義一個基本類型 Animal，以及一個子類型 Dog，展示多態的行為。

def process_text(input_text):
    words = input_text.split()
    filtered_words = [word for word in words if len(word) >= 3]
    sorted_words = sorted(filtered_words, key=len)
    return sorted_words

if __name__ == "__main__":
    text = "This is an example of text processing in Python"
    result = process_text(text)
    print("Processed words:", result)
