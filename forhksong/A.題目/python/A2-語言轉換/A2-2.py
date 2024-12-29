##A2題形-生成器與迭代器
##功能：實現一個生成器函數，用於生成指定範圍內的所有奇數。

def odd_numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 != 0:
            yield num

if __name__ == "__main__":
    start, end = 1, 10
    print("Odd numbers from {} to {}:".format(start, end))
    for odd in odd_numbers(start, end):
        print(odd)

