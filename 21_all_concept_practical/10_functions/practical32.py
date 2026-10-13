# Task:
# 1. sort_by_last_char(words) naam ka function banao.
# 2. Function ke andar sorted() aur key=lambda word: word[-1] use karo.
# 3. Words ko unke last character ke according ascending order mein sort karke return karo.
# 4. Function ko ["apple", "banana", "kiwi", "mango"] ke saath call karo aur result print karo.
# Expected output:
# ['banana', 'apple', 'mango', 'kiwi']

def sort_by_last_char(words):
    return sorted(words, key= lambda word : word[-1])

print(sort_by_last_char(["apple", "banana", "kiwi", "mango"]))