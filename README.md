# SpendSmart

## Introduction
The SpendSmart is a Python-based application that allows users to track their daily expenses, set budgets, add to savings, and generate account statements. The program is designed to be user-friendly and helps users manage their finances effectively.

## Features
- Add and categorize expenses
- Search expenses by date or item
- Set and track budget
- Add to savings
- View account statement (expense details, category totals, grand total, savings, and budget)
- Save expenses to a JSON file
- Export expenses to an Excel file
- Reset all data

## Requirements
- Python 3.x
- pandas
- tabulate

## Installation
1. Clone the repository or download the source code.
2. Install the required Python packages:
    ```sh
    pip install pandas tabulate
    ```

## Usage
1. Run the `expense_tracker.py` script to start the program:
    ```sh
    python expense_tracker.py
    ```

2. Follow the on-screen prompts to interact with the program.

## Options
- **Add expense:** Add a new expense with a name, amount, and category.
- **Search expenses:** Search expenses by date or item.
- **Set budget and track:** Set a budget and track expenses against the budget.
- **Add to savings:** Add a specified amount to your savings.
- **Account statement:** View the total spent, savings, budget, expense details, category totals, and grand total.
- **Save and Exit:** Save the current expenses to a JSON file and exit to the main menu.
- **Reset:** Reset all expenses, budget, and savings data.

## Example
```sh
1. Add expense
2. Search expenses (by date or item)
3. Set budget and track
4. Add to savings
5. Account statement
6. Save and Exit
7. Reset
Enter choice: 1
Enter expense name: Lunch
Enter expense amount: ₹200
Choose a category:
1. Groceries
2. Entertainment
3. Bills
4. Transport
5. Others
Enter category number: 2
1. Add another expense
2. Skip
Enter choice: 1
...
