import datetime

class Banking_App:

    def __init__(self, initial_balance=0.00):
        self.balance = initial_balance


    def transaction_log(self, transaction_string):
        with open("transaction_history.txt", "a") as file:
            file.write(f"{transaction_string}\n")
    

    def withdrawal(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            if amount > self.balance:
                print(f"Insufficient funds. Maximum withdrawal: €{self.balance}")
        else:
            self.balance = self.balance - amount
            x = datetime.datetime.now()
            cur_time = x.strftime("%d/%b/%Y - %I:%M%p")
            self.transaction_log(f"\n{cur_time}:\nWithdrawal: €{amount}. \t\t\tNew balance: €{self.balance}")

    
    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance + amount
            x = datetime.datetime.now()
            cur_time = x.strftime("%d/%b/%Y - %I:%M%p")
            self.transaction_log(f"\n{cur_time}:\nDeposit: €{amount}. \t\t\tNew Balance: €{self.balance}")

account = Banking_App(00.00)

while True:
    try:
        action = input("\nWelcome to your bank account. What would you like to do?\n\t1.Withdrawal\n\t2.Deposit\n\t3.Display Balance\n\t4.Exit\n\nChoose an option: ")
    except KeyboardInterrupt:
        print("\nThank you, goodbye.")
        break
    if action in ["1", "2", "3", "4"]:
        if action == "1":
            try:
                amount = input("How much would you like to withdraw?\t€")
                account.withdrawal(amount)
                print(f"Balance: \t€{account.balance}.")
            except KeyboardInterrupt:
                print("\nThank you, goodbye.")
                break
        elif action == "2":
            try:
                amount = input("How much would you like to deposit?\t€")
                account.deposit(amount)
                print(f"Balance: \t€{account.balance}.")
            except KeyboardInterrupt:
                print("\nThank you, goodbye.")
                break
        elif action == "3":
            try:
                print(f"Balance: \t€{account.balance}.")
            except KeyboardInterrupt:
                print("\nThank you, goodbye.")
                break
        elif     action == "4":
            try:
                print("Thank you, goodbye.")
                break
            except KeyboardInterrupt:
                print("\nThank you, goodbye.")
                break
    else:
        print("Invalid input. You will now be returned to the main menu.")