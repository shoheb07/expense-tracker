# Simple Expense Tracker (Python CLI)

import datetime

expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, Rent, etc.): ")
    note = input("Enter note (optional): ")
    date = datetime.date.today()

    expenses.append({
        "amount": amount,
        "category": category,
        "note": note,
        "date": date
    })

    print("Expense added successfully.")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- Expense List ---")
    for i, exp in enumerate(expenses, start=1):
        print(
            f"{i}. ₹{exp['amount']} | {exp['category']} | "
            f"{exp['note']} | {exp['date']}"
        )

def total_expense():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Expense: ₹{total}")

def main():
    while True:
        print("\n=== EXPENSE TRACKER ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            print("Exiting Expense Tracker.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
