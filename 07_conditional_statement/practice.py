import random

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

random_number = random.randint(start, end)

guess = int(input(f"Guess a number between {start} and {end}: "))

if guess == random_number:
    print("Congratulations! Your guess is correct.")

elif guess > random_number:
    print("Your guess is too high.")
    print("The correct number was:", random_number)

else:
    print("Your guess is too low.")
    print("The correct number was:", random_number)