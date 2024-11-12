import random

options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    cpu = random.choice(options)

    while player not in options:
        player = input(f"Choose within {options} or 'q' to quit: ")

        if player.lower() == "q":
            print("You quit the game.")
            running = False  # Set running to False to exit the main loop
            break

        if player not in options:
            print("Invalid choice, try again.")

    # If player chose to quit, skip the rest of the loop
    if not running:
        break

    print(f"Player: {player}")
    print(f"Cpu: {cpu}")

    if player == cpu:
        print("TIE!")
    elif (player == "rock" and cpu == "scissors") or (player == "paper" and cpu == "rock") or (player == "scissors" and cpu == "paper"):
        print("You Win")
    else:
        print("You Lose")

    if input("Play again? (y/n): ").lower() != "y":
        running = False

print("Thanks for playing!")
