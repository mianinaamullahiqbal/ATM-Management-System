#ATM MANAGEMENT SYSTEM PROJECT BY {MIAN INAAMULLAH IQBAL & M. SAQIB JAVED}
#REG NO : L1F24BSSE0004 & L1F24BSSE0007
#SEC : M-10

class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, pin, balance=0):
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            if len(pin) != 4 or not pin.isdigit():
                print("PIN must be a 4-digit number.")
                return
            self.accounts[account_number] = {'pin': pin, 'balance': balance}
            print("Account created successfully.")

    def authenticate(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account and account['pin'] == pin:
            return True
        return False

    def check_balance(self, account_number):
        balance = self.accounts[account_number]['balance']
        print(f"Your current balance is: {balance}")
        return balance

    def deposit(self, account_number, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            self.accounts[account_number]['balance'] += amount
            print(f"Deposited {amount}. New balance: {self.accounts[account_number]['balance']}")

    def withdraw(self, account_number, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.accounts[account_number]['balance']:
            print("Insufficient balance.")
        else:
            self.accounts[account_number]['balance'] -= amount
            print(f"Withdrawn {amount}. Remaining balance: {self.accounts[account_number]['balance']}")

def main():
    atm = ATM()
    while True:
        print("\nATM Management System")
        print("1. Create Account")
        print("2. Access Account")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            account_number = input("Enter account number: ").strip()
            if not account_number.isdigit():
                print("Account number must be numeric.")
                continue
            pin = input("Set a 4-digit PIN: ").strip()
            initial_deposit = input("Enter initial deposit (optional, default 0): ").strip()
            try:
                initial_deposit = float(initial_deposit) if initial_deposit else 0
            except ValueError:
                print("Invalid deposit amount.")
                continue
            atm.create_account(account_number, pin, initial_deposit)
        elif choice == '2':
            account_number = input("Enter account number: ").strip()
            if not account_number.isdigit():
                print("Account number must be numeric.")
                continue
            pin = input("Enter PIN: ").strip()
            if atm.authenticate(account_number, pin):
                while True:
                    print("\nAccount Menu")
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Exit")
                    account_choice = input("Choose an option: ").strip()
                    if account_choice == '1':
                        atm.check_balance(account_number)
                    elif account_choice == '2':
                        amount = input("Enter amount to deposit: ").strip()
                        try:
                            amount = float(amount)
                            atm.deposit(account_number, amount)
                        except ValueError:
                            print("Invalid amount. Please enter a numeric value.")
                    elif account_choice == '3':
                        amount = input("Enter amount to withdraw: ").strip()
                        try:
                            amount = float(amount)
                            atm.withdraw(account_number, amount)
                        except ValueError:
                            print("Invalid amount. Please enter a numeric value.")
                    elif account_choice == '4':
                        print("Exiting account menu.")
                        break
                    else:
                        print("Invalid option. Please try again.")
            else:
                print("Invalid account number or PIN.")
        elif choice == '3':
            print("Exiting ATM Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
