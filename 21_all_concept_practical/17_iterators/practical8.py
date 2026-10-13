# Ek generator function count_up(start=1) banao jo:
# 1. while True se numbers infinitely generate kare.
# 2. Har iteration mein current number yield kare.
# 3. Number ko increment kare.
# 4. itertools module se islice() import karo.
# 5. islice() se infinite generator ke sirf pehle 10 numbers nikalo.
# 6. Un numbers ko list mein convert karke print karo.
# 7. Ek doosre generator se islice() ka use karke 5 se 10 tak numbers nikalo.
# Expected output
# First 10 numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Numbers from 5 to 10: [5, 6, 7, 8, 9, 10]


from itertools import islice


def count_up(start=1):
    number = start

    while True:
        yield number
        number += 1


# Test 1: Pehle 10 numbers
generator1 = count_up()
first_10 = list(islice(generator1, 10))
print("First 10 numbers:", first_10)

# Test 2: Numbers 5 se 10 tak
generator2 = count_up()
numbers_5_to_10 = list(islice(generator2, 4, 10))
print("Numbers from 5 to 10:", numbers_5_to_10)
