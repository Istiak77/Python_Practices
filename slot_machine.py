import random

def spin_row():
    symbols = ['A','B','C','D','E']

    results = []

    return [random.choice(symbols) for symbol in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == 'A':
            return bet * 20
        elif row[0] == 'B':
            return bet * 10
        elif row[0] == 'C':
            return bet * 8
        elif row[0] == 'D':
            return bet * 5
        elif row[0] == 'E':
            return bet * 2
    return 0

def main():
    balance = 100

    print("Welcome to python slots")
    print("Symbols: A B C D E")

    while balance > 0:
        print(f"Current balance: {balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet greater than 0")
            continue
        
        balance -= bet

        row = spin_row()

        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"\nYou won {payout}\n")
        else:
            print(f"\nYou lost {bet}\n")
        
        balance += payout

        play_again = input("Play again?(Y/N): ").upper()

        if play_again != 'Y':
            break
        print(f"Your final balance is {balance}")

if __name__ == '__main__':
    main()