from account.transaction import Transaction
from account.user import User

class BankAccount:
    def __init__(self, name="John", email="john@gmail.com", initial_balance=0, account_type="Generic"):
        self.balance = initial_balance
        self.transactions_history = []
        self.account_type = account_type
        self.user = User(name, email)

    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Deposit amount is invalid!")
            return
        self.balance += amount
        self.transactions_history.append(Transaction(amount, "deposit"))

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Withdrawal amount is invalid!")
            return
        if self.balance < amount:
            print("Insufficient Balance!")
            return
        self.balance -= amount
        self.transactions_history.append(Transaction(amount, "withdraw"))

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions_history

    def get_account_type(self):
        return self.account_type

    def get_user(self):
        return self.user

class SavingsAccount(BankAccount):
    MIN_BALANCE = 100

    def withdraw(self, amount):
        if self.balance - amount < self.MIN_BALANCE:
            print("Insufficient funds: Minimum balance of Rs.100 is required!")
            return
        super().withdraw(amount)

    def get_account_type(self):
        return "Savings account"

class CurrentAccount(BankAccount):
    def get_account_type(self):
        return "Current account"

class StudentAccount(BankAccount):
    MIN_BALANCE = 100

    def withdraw(self, amount):
        if self.balance - amount < self.MIN_BALANCE:
            print("A minimum balance of Rs.100 needed to withdraw from a Student account!")
            return
        super().withdraw(amount)

    def get_account_type(self):
        return "Student account"


# Function to create an account based on user selection
def create_account(users):
    if not users:
        print("No users available. Please create a user first.")
        return

    user = select_user(users)
    if not user:
        return
    
    account_type = input("Enter account type (Savings, Current, Student): ").lower()
    if account_type not in ["savings", "current", "student"]:
        print("Invalid account type!")
        return

    # Based on the account type, create the respective account
    if account_type == "savings":
        account = SavingsAccount(user.name, user.email)
    elif account_type == "current":
        account = CurrentAccount(user.name, user.email)
    elif account_type == "student":
        account = StudentAccount(user.name, user.email)

    print(f"Account created for {user.name} ({account.get_account_type()})")

# Function to handle user selection and validation
def select_user(users):
    if not users:
        print("No users available. Please create a user first.")
        return None
    try:
        user_index = int(input("Select user number: "))
        if user_index < 0 or user_index >= len(users):
            print("Invalid user selection.\n")
            return None
        return users[user_index]
    except ValueError:
        print("Please enter a valid number.")
        return None

# Sample usage:
users = [User("Alice", "alice@example.com"), User("Bob", "bob@example.com")]  # Example users
create_account(users)  # Create an account by selecting a user
