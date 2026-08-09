import json
import os
from datetime import datetime


DATA_FILE = "finance_data.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_data(transactions):
    with open(DATA_FILE, "w") as file:
        json.dump(transactions, file, indent=4)


def get_amount():
    while True:
        try:
            amount = float(input("Enter amount: ₹"))

            if amount <= 0:
                print("❌ Amount must be greater than 0.")
                continue

            return amount

        except ValueError:
            print("❌ Please enter a valid amount.")


def get_date():
    while True:
        date = input("Enter date (DD-MM-YYYY) or press Enter for today: ")

        if not date:
            return datetime.now().strftime("%d-%m-%Y")

        try:
            datetime.strptime(date, "%d-%m-%Y")
            return date
        except ValueError:
            print("❌ Invalid date. Use DD-MM-YYYY.")


def add_transaction(transactions):
    print("\n--- Add Transaction ---")
    print("1. Income")
    print("2. Expense")

    transaction_type = input("Choose type (1/2): ")

    if transaction_type == "1":
        transaction_type = "Income"
    elif transaction_type == "2":
        transaction_type = "Expense"
    else:
        print("❌ Invalid choice.")
        return

    category = input("Enter category: ").strip()

    if not category:
        print("❌ Category cannot be empty.")
        return

    description = input("Enter description: ").strip()

    if not description:
        print("❌ Description cannot be empty.")
        return

    amount = get_amount()
    date = get_date()

    transaction = {
        "id": len(transactions) + 1,
        "type": transaction_type,
        "category": category,
        "description": description,
        "amount": amount,
        "date": date
    }

    transactions.append(transaction)
    save_data(transactions)

    print("\n✅ Transaction added successfully!")


def view_transactions(transactions):
    print("\n" + "=" * 85)
    print("                         TRANSACTIONS")
    print("=" * 85)

    if not transactions:
        print("No transactions found.")
        return

    print(
        f"{'ID':<5}"
        f"{'Date':<15}"
        f"{'Type':<12}"
        f"{'Category':<18}"
        f"{'Description':<20}"
        f"{'Amount':>12}"
    )

    print("-" * 85)

    for transaction in transactions:
        print(
            f"{transaction['id']:<5}"
            f"{transaction['date']:<15}"
            f"{transaction['type']:<12}"
            f"{transaction['category']:<18}"
            f"{transaction['description']:<20}"
            f"₹{transaction['amount']:>10.2f}"
        )

    print("=" * 85)


def show_summary(transactions):
    total_income = sum(
        transaction["amount"]
        for transaction in transactions
        if transaction["type"] == "Income"
    )

    total_expense = sum(
        transaction["amount"]
        for transaction in transactions
        if transaction["type"] == "Expense"
    )

    balance = total_income - total_expense

    print("\n" + "=" * 45)
    print("              FINANCIAL SUMMARY")
    print("=" * 45)
    print(f"Total Income   : ₹{total_income:.2f}")
    print(f"Total Expense  : ₹{total_expense:.2f}")
    print(f"Current Balance: ₹{balance:.2f}")
    print("=" * 45)


def category_summary(transactions):
    if not transactions:
        print("\nNo transactions found.")
        return

    categories = {}

    for transaction in transactions:
        if transaction["type"] == "Expense":
            category = transaction["category"]
            amount = transaction["amount"]

            categories[category] = categories.get(category, 0) + amount

    if not categories:
        print("\nNo expenses found.")
        return

    print("\n--- Expense By Category ---")

    for category, amount in sorted(
        categories.items(),
        key=lambda item: item[1],
        reverse=True
    ):
        print(f"{category:<20} ₹{amount:.2f}")


def search_transactions(transactions):
    keyword = input("\nEnter keyword to search: ").strip().lower()

    if not keyword:
        print("❌ Search keyword cannot be empty.")
        return

    results = []

    for transaction in transactions:
        searchable_text = (
            f"{transaction['type']} "
            f"{transaction['category']} "
            f"{transaction['description']} "
            f"{transaction['date']}"
        ).lower()

        if keyword in searchable_text:
            results.append(transaction)

    if results:
        print(f"\n🔎 Found {len(results)} transaction(s):")
        view_transactions(results)
    else:
        print("❌ No matching transactions found.")


def delete_transaction(transactions):
    view_transactions(transactions)

    if not transactions:
        return

    try:
        transaction_id = int(input("\nEnter transaction ID to delete: "))

        for transaction in transactions:
            if transaction["id"] == transaction_id:
                transactions.remove(transaction)
                save_data(transactions)

                # Reassign IDs
                for index, item in enumerate(transactions, start=1):
                    item["id"] = index

                save_data(transactions)

                print("🗑️ Transaction deleted successfully!")
                return

        print("❌ Transaction ID not found.")

    except ValueError:
        print("❌ Please enter a valid ID.")


def monthly_summary(transactions):
    month = input("\nEnter month (MM-YYYY): ").strip()

    try:
        datetime.strptime(month, "%m-%Y")
    except ValueError:
        print("❌ Invalid format. Use MM-YYYY.")
        return

    monthly_transactions = [
        transaction
        for transaction in transactions
        if transaction["date"][3:] == month
    ]

    if not monthly_transactions:
        print("No transactions found for this month.")
        return

    income = sum(
        transaction["amount"]
        for transaction in monthly_transactions
        if transaction["type"] == "Income"
    )

    expense = sum(
        transaction["amount"]
        for transaction in monthly_transactions
        if transaction["type"] == "Expense"
    )

    print("\n" + "=" * 45)
    print(f"          MONTHLY SUMMARY: {month}")
    print("=" * 45)
    print(f"Income  : ₹{income:.2f}")
    print(f"Expense : ₹{expense:.2f}")
    print(f"Balance : ₹{income - expense:.2f}")
    print("=" * 45)


def main():
    transactions = load_data()

    while True:
        print("\n" + "=" * 50)
        print("           PERSONAL FINANCE MANAGER")
        print("=" * 50)
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Financial Summary")
        print("4. Category-wise Expenses")
        print("5. Search Transactions")
        print("6. Monthly Summary")
        print("7. Delete Transaction")
        print("8. Exit")
        print("=" * 50)

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_transaction(transactions)

        elif choice == "2":
            view_transactions(transactions)

        elif choice == "3":
            show_summary(transactions)

        elif choice == "4":
            category_summary(transactions)

        elif choice == "5":
            search_transactions(transactions)

        elif choice == "6":
            monthly_summary(transactions)

        elif choice == "7":
            delete_transaction(transactions)

        elif choice == "8":
            print("\n👋 Thanks for using Personal Finance Manager!")
            break

        else:
            print("❌ Invalid choice. Please select 1-8.")


if __name__ == "__main__":
    main()
