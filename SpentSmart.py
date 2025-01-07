import datetime
import json
import pandas as pd
from tabulate import tabulate

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.initial_balance = None
        self.budget = None
        self.savings = 0
        self.categories = ["Groceries", "Entertainment", "Bills", "Transport", "Others"]
        self.transactions = []
        print("Welcome! ExpenseTracker initialized.")

    def add_expense(self, name, amount, category):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        expense = {"name": name, "amount": amount, "date": date, "category": category}
        self.expenses.append(expense)
        self.transactions.append((date, 'Expense', amount, category))
        print(f"Added expense: {expense}")

    def track_budget(self):
        if self.budget is None:
            print("No budget set. Please set a budget first.")
            return

        total_spent = sum(expense['amount'] for expense in self.expenses)
        if total_spent > self.budget:
            print(f"Warning: You have exceeded your budget by ₹{total_spent - self.budget}")
        else:
            print(f"Total spent: ₹{total_spent}. You are within your budget.")

    def account_statement(self):
        total_spent = sum(expense['amount'] for expense in self.expenses)
        category_totals = {category: 0 for category in self.categories}
        for expense in self.expenses:
            category_totals[expense['category']] += expense['amount']

        df_expenses = pd.DataFrame(self.expenses)
        category_totals_df = pd.DataFrame(list(category_totals.items()), columns=['Category', 'Total'])
        grand_total_df = pd.DataFrame([{'Category': 'Grand Total', 'Total': total_spent}])

        statement = [
            {"Description": "Total Spent", "Amount": f"₹{total_spent}"},
            {"Description": "Savings", "Amount": f"₹{self.savings}"},
            {"Description": "Budget", "Amount": f"₹{self.budget}" if self.budget is not None else "Not Set"}
        ]

        df_statement = pd.DataFrame(statement)
        
        print("\nExpense Details:")
        print(tabulate(df_expenses, headers='keys', tablefmt='pretty', showindex=False))

        print("\nCategory Totals:")
        print(tabulate(category_totals_df, headers='keys', tablefmt='pretty', showindex=False))

        print("\nGrand Total:")
        print(tabulate(grand_total_df, headers='keys', tablefmt='pretty', showindex=False))

        print("\nAccount Statement:")
        print(tabulate(df_statement, headers='keys', tablefmt='pretty', showindex=False))

    def save_expenses(self, filename="expenses.json"):
        with open(filename, "w", encoding='utf-8') as f:
            json.dump(self.expenses, f)
        print(f"Expenses saved to {filename}")

    def load_expenses(self, filename="expenses.json"):
        try:
            with open(filename, "r", encoding='utf-8') as f:
                self.expenses = json.load(f)
            print(f"Expenses loaded from {filename}")
        except FileNotFoundError:
            self.expenses = []
            print(f"{filename} not found. Starting with an empty expenses list.")

    def save_to_excel(self, filename="expenses.xlsx"):
        df = pd.DataFrame(self.expenses)
        df.to_excel(filename, index=False)
        print(f"Expenses saved to {filename}")

    def search_expenses_by_date(self, search_date):
        search_date_str = search_date.strftime("%Y-%m-%d")
        results = [expense for expense in self.expenses if expense['date'].startswith(search_date_str)]
        if results:
            df = pd.DataFrame(results)
            print("\nSearch Results by Date:")
            print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))
        else:
            print("No expenses found for the given date.")
        return results

    def search_expenses_by_item(self, item_name):
        results = [expense for expense in self.expenses if expense['name'].lower() == item_name.lower()]
        if results:
            df = pd.DataFrame(results)
            print("\nSearch Results by Item:")
            print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))
        else:
            print("No expenses found for the given item.")
        return results

    def set_budget(self, amount):
        self.budget = amount
        print(f"Budget set to ₹{self.budget}")

    def add_to_savings(self, amount):
        self.savings += amount
        print(f"Added ₹{amount} to savings. Total savings: ₹{self.savings}")

    def reset_expenses(self):
        self.expenses = []
        self.initial_balance = None
        self.budget = None
        self.savings = 0
        self.transactions = []
        print("All expenses, initial balance, and other data have been reset.")

def main():
    tracker = ExpenseTracker()
    tracker.load_expenses()

    while True:
        print("Main Menu")
        print("\n1. Add expense\n2. Search expenses (by date or item)\n3. Set budget and track\n4. Add to savings\n5. Account Statement\n6. Save and Exit\n7. Reset")
        choice = input("Enter choice: ")
        print(f"User selected choice {choice}")
        if choice == '1':
            while True:
                name = input("Enter expense name: ")
                amount = float(input("Enter expense amount: ₹"))
                print("\nChoose a category:")
                for i, category in enumerate(tracker.categories, 1):
                    print(f"{i}. {category}")
                category_choice = int(input("Enter category number: "))
                category = tracker.categories[category_choice - 1]
                tracker.add_expense(name, amount, category)
                print("1. Add another expense\n2. Skip")
                another_choice = input("Enter choice: ")
                if another_choice != '1':
                    break
        elif choice == '2':
            print("\n1. Search by date\n2. Search by item")
            search_choice = input("Enter choice: ")
            if search_choice == '1':
                search_date = input("Enter date (YYYY-MM-DD): ")
                search_date = datetime.datetime.strptime(search_date, "%Y-%m-%d")
                tracker.search_expenses_by_date(search_date)
            elif search_choice == '2':
                item_name = input("Enter item name: ")
                tracker.search_expenses_by_item(item_name)
            else:
                print("Invalid choice.")
        elif choice == '3':
            print("\n1. Set budget\n2. Track budget")
            budget_choice = input("Enter choice: ")
            if budget_choice == '1':
                amount = float(input("Enter budget amount: ₹"))
                tracker.set_budget(amount)
            elif budget_choice == '2':
                tracker.track_budget()
            else:
                print("Invalid choice.")
        elif choice == '4':
            amount = float(input("Enter amount to add to savings: ₹"))
            tracker.add_to_savings(amount)
        elif choice == '5':
            tracker.account_statement()
        elif choice == '6':
            tracker.save_expenses()
            break
        elif choice == '7':
            tracker.reset_expenses()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
