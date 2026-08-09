import csv
import os


FILE_NAME = "expenses.csv"


def load_expenses():
    expenses = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                expenses.append(row)

    return expenses


def save_expenses(expenses):
    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["date", "category", "description", "amount"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(expenses)


def add_expense(expenses):
    print("\n--- Add Expense ---")

    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    description = input("Enter description: ")

    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid amount.")

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": f"{amount:.2f}"
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("✅ Expense added successfully!")


def view_expenses(expenses):
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses found.")
        return

    print("-" * 70)
    print(f"{'Date':<15}{'Category':<15}{'Description':<25}{'Amount':>10}")
    print("-" * 70)

    for expense in expenses:
        print(
            f"{expense['date']:<15}"
            f"{expense['category']:<15}"
            f"{expense['description']:<25}"
            f"₹{float(expense['amount']):>9.2f}"
        )

    print("-" * 70)


def show_total(expenses):
    total = sum(float(expense["amount"]) for expense in expenses)

    print("\n--- Expense Summary ---")
    print(f"Total expenses: ₹{total:.2f}")


def category_summary(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = float(expense["amount"])

        categories[category] = categories.get(category, 0) + amount

    print("\n--- Category Summary ---")

    for category, amount in categories.items():
        print(f"{category}: ₹{amount:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n" + "=" * 45)
        print("          EXPENSE TRACKER")
        print("=" * 45)
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            show_total(expenses)

        elif choice == "4":
            category_summary(expenses)

        elif choice == "5":
            print("\n👋 Thank you for using Expense Tracker!")
            break

        else:
            print("❌ Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
