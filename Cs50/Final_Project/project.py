import sys

def main():
    print("Welcome to the Budget Tracker!")
    while True:
        print("\nOptions:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Summary")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_income()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            print(f"Current Balance: ${get_balance()}")
        elif choice == '4':
            print_summary()
        elif choice == '5':
            sys.exit()
        else:
            print("Invalid choice, please try again.")

transactions=[]

def add_income():
    amount = float(input("Enter income amount: "))
    description = input("Enter income description: ")
    transactions.append({"type": "income", "amount": amount, "description": description})
    print("Income added successfully.")

def add_expense():
    amount = float(input("Enter expense amount: "))
    description = input("Enter expense description: ")
    transactions.append({"type": "expense", "amount": amount, "description": description})
    print("Expense added successfully.")

def get_balance():
    balance = 0
    for transaction in transactions:
        if transaction["type"] == "income":
            balance += transaction["amount"]
        elif transaction["type"] == "expense":
            balance -= transaction["amount"]
    return balance

def print_summary():
    print("\nTransaction Summary:")
    for transaction in transactions:
        print(f"{transaction['type'].capitalize()}: ${transaction['amount']} ({transaction['description']})")
    print(f"Total Balance: ${get_balance()}")



if __name__ == "__main__":
    main()
