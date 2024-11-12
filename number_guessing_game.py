import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")
print("Press 'q' to quit the game.")

while is_running:

    guess = input("Enter a guess: ")

    if guess.lower() == 'q':
        print("Thanks for playing! Goodbye.")
        break

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("Out of range")
            print(f"Select a number between {lowest_num} and {highest_num}")

        elif guess < answer:
            print("Too low")
        elif guess > answer:
            print("Too high")
        else:
            print(f"You got it! The number was {answer}")
            print(f"Attempts taken: {guesses}")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Select a number between {lowest_num} and {highest_num}")
