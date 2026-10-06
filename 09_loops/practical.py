# For loop Example

import random

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

random_number = random.randint(start, end)

for chance in range(1, 6):

    guess = int(input(f"Chance {chance}/5 - Guess the number: "))

    if guess == random_number:
        print("Congratulations! Correct guess.")
        break

    elif guess > random_number:
        print("Too High!")

    else:
        print("Too Low!")

else:
    print("Game Over!")
    print("The correct number was:", random_number)


# While loop example

# correct_password = "python"

# attempt = 1

# while attempt <= 5:

#     password = input("Enter password: ")

#     if password == correct_password:
#         print("Login successful!")
#         break

#     else:
#         print("Incorrect password.")

#     attempt += 1

# else:
#     print("Account locked. Too many attempts.")