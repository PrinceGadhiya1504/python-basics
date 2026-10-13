# CountUp class banao jo __iter__() aur __next__() implement kare aur 1 se limit tak count kare.
# Yaad rahe:
# - CountUp(5) → 1, 2, 3, 4, 5
# - list(CountUp(3)) → [1, 2, 3]

class CountUp:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration

        number = self.current
        self.current += 1
        return number



# Test 1: 1 se 5 tak count
for number in CountUp(5):
    print(number)