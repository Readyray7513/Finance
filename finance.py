import json
from datetime import datetime

class BudgetTracker:
    def __init__(self, income):
        self.income = income
        self.expenses = []
        self.categories = {"Needs": 0.5, "Wants": 0.3, "Savings": 0.2}
        self.balance = income

    def add_expense(self, amount, category, description):
        if category not in self.categories:
            print("Invalid category! Choose from: Needs, Wants, Savings")
            return
        if amount > self.balance:
            print("Not enough balance!")
            return
        self.expenses.append({
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        self.balance -= amount
        print(f"Added expense: £{amount} for {description} under {category}")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        for exp in self.expenses:
            print(f"{exp['date']} | £{exp['amount']} | {exp['category']} | {exp['description']}")

    def summary(self):
        spent = sum(exp["amount"] for exp in self.expenses)
        print("\n--- Budget Summary ---")
        print(f"Total Income: £{self.income}")
        print(f"Total Spent: £{spent}")
        print(f"Remaining Balance: £{self.balance}")
        
        cat_totals = {cat: 0 for cat in self.categories}
        for exp in self.expenses:
            cat_totals[exp['category']] += exp['amount']
        
        print("\nCategory Breakdown:")
        for cat, amount in cat_totals.items():
            print(f"{cat}: £{amount} (Recommended: £{self.income * self.categories[cat]})")

    def save_data(self, filename="budget_data.json"):
        data = {"income": self.income, "expenses": self.expenses, "balance": self.balance}
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print("Budget data saved successfully!")

    def load_data(self, filename="budget_data.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.income = data["income"]
                self.expenses = data["expenses"]
                self.balance = data["balance"]
                print("Budget data loaded successfully!")
        except FileNotFoundError:
            print("No previous data found, starting fresh.")


# Example usage:
if __name__ == "__main__":
    income = float(input("Enter your monthly income: £"))
    budget = BudgetTracker(income)
    budget.load_data()
    
    while True:
        print("\nOptions: 1) Add Expense  2) View Expenses  3) Summary  4) Save & Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            amount = float(input("Enter expense amount: £"))
            category = input("Enter category (Needs, Wants, Savings): ")
            description = input("Enter description: ")
            budget.add_expense(amount, category, description)
        elif choice == "2":
            budget.view_expenses()
        elif choice == "3":
            budget.summary()
        elif choice == "4":
            budget.save_data()
            break
        else:
            print("Invalid choice, try again!")
