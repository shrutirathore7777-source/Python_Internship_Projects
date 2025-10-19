def bank_system():
    accounts = {} # stores accounts as {username : [pin, balance]}
    def create_accounts():
        name = input("Enter you name: ").strip()
        if name in accounts:
            print("Account with this name alraedy exists!")
            return
        pin = input("Set a 4 digit PIN: ")
        if not pin.isdigit or len(pin) != 4:
            print("PIN must be exactly 4 digits(numbers only)!")
            return
        accounts[name] = [pin,0.0]
        print(f"Account created successfully for {name}")

    def deposit(name):
        try:
            amount = float(input("Enter ammount to deposit: "))
            if amount <= 0:
                print("Deposit ammount must be positive!")
                accounts[name][1] += amount
                print(f"₹{amount} deposited successfully!")
        except ValueError:
                print("Please enter a valid number!")
        
    def withdraw(name):
        try :
            amount = float(input("Enter a amount to withdraw: "))
            if amount <= 0:
                    print("Withdraw amount must be positive!")
                    return
            if amount<= accounts[name][1]:
                    accounts[name][1] -= amount
                    print(f"₹ {amount} withdraw successfully!")
            else:
                    print("Insufficient balance!")
        except ValueError:
                print("Please enter a valid number!")

    def check_balance(name):
        print(f"Current balance: ₹ {accounts[name][1]}")

    while True:
        print("\n MINI BANK SYSTEM")
        print("1. Create account\n2. Login\n3. Exit")
        choice = input ( "Enter your choice: ").strip()
        if choice =="1":
            create_accounts()
        elif choice == "2":
            name = input("Enter your name: ").strip()
            pin = input("Enter PIN: ")
            if name in accounts and accounts[name][0] == pin:
                print(f"Welcome{name}! Login successful")

                while True:
                    print("\n---Banking Menu ---")
                    print("1.Deposit\n2.Withdraw\n3.Check balance\n 4.Logout")
                    option = input("Enter your choice: ")
                    if option == "1":
                        deposit(name)
                    elif option == "2":
                        withdraw(name)
                    elif option == "3":
                        check_balance(name)
                    elif option == "4":
                        print("Logging out..")
                        break
                    else:
                        print("Invalid option! Try again.")
            else:
                print("Invalid login details ! please check your name or PIN")
        elif choice == "3":
            print("Exiting Bank system....")
        else:
            print("Invalid choice! Please enter 1,2, or 3.")
bank_system()             