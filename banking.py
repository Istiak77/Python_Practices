def show_balance(balance):
    print(f"Your balance is {balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to deposit: "))

    if amount < 0:
        print("Invalid ammount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount  = float(input("Enter an ammount to withdraw: "))

    if amount > balance:
        print("Insufficient Funds")
        return 0
    elif amount < 0:
        print("Amount must be more than 0")
        return 0
    else:
        return amount

def main():

    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        option = input("Enter an option (1-4): ")

        if option == "1":
            show_balance(balance)
        elif option == "2":
            balance += deposit()
        elif option == "3":
            balance -= withdraw(balance)
        elif option == "4":
            is_running = False
        else:
            print("Invalid option")

    print("Thank you for using this program")

if __name__ == '__main__':
    main()