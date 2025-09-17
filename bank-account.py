def menu():
    print("1 - Deposit ")
    print("2 - Withdraw")
    print("3 - Balance ")
    print("4 - Exit    ")


def deposit(wallet):
    try:
        add = float(input("How much do you want to deposit: "))
        if add > 0:
            wallet += add
            print(f" Updated deposit! Now you have ${wallet:.2f}")
        else:
            print(" Enter a positive number!")
    except ValueError:
        print(" Enter a valid number!")
    return wallet


def withdraw(wallet):
    print(f" You have R${wallet:.2f} in your wallet")
    try:
        remove = float(input("How much do you want to withdraw: "))
        if remove <= 0:
            print(" Enter a positive number!")
        elif remove <= wallet:
            wallet -= remove
            print(f" Updated withdraw! Now you have ${wallet:.2f}")
        else:
            print(" Insufficient funds!")
    except ValueError:
        print(" Please enter a valid number!")
    return wallet


def show_balance(wallet):
    print(f" Your total balance is R${wallet:.2f}")



wallet = 0

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        wallet = deposit(wallet)
    elif choice == "2":
        wallet = withdraw(wallet)
    elif choice == "3":
        show_balance(wallet)
    elif choice == "4":
        print(" Bye")
        break
    else:
        print(" Enter a valid option")


