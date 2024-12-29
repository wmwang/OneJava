##A3題型:  非必要的重複排序
##效能問題：多次對同一列表排序，浪費資源
def process_data(data):
    sorted_data = sorted(data)
    return sorted_data[-1], sorted_data[0]

if __name__ == "__main__":
    data = [5, 3, 8, 6, 7, 2, 4, 1] * 10000
    max_val, min_val = process_data(data)  # 每次都進行排序
    print(f"Max: {max_val}, Min: {min_val}")


