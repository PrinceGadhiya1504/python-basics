# Task:
# 1. sort_by_length(words) naam ka function banao.
# 2. Function ko words ki list milegi: ["apple", "kiwi", "banana", "fig"].
# 3. sorted() aur key=len ka use karke words ko length ke according ascending order mein sort karo.
# 4. Sorted list return karo aur print karo.
# Expected output:
# ['fig', 'kiwi', 'apple', 'banana']

def sort_by_length(words):
    return sorted(words, key = len)

print(sort_by_length(["apple", "kiwi", "banana", "fig"]))