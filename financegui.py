from PyQt6 import QtWidgets, QtGui, QtCore
import json
import sys

class BudgetTrackerApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Budget Tracker")
        self.setGeometry(100, 100, 500, 400)
        self.income = 0
        self.expenses = []
        self.balance = 0
        self.load_data()
        self.initUI()

    def initUI(self):
        layout = QtWidgets.QVBoxLayout()
        
        self.income_label = QtWidgets.QLabel(f"Monthly Income: £{self.income}")
        layout.addWidget(self.income_label)
        
        self.balance_label = QtWidgets.QLabel(f"Balance: £{self.balance}")
        layout.addWidget(self.balance_label)
        
        self.expense_list = QtWidgets.QListWidget()
        self.update_expense_list()
        layout.addWidget(self.expense_list)
        
        self.amount_input = QtWidgets.QLineEdit()
        self.amount_input.setPlaceholderText("Enter amount")
        layout.addWidget(self.amount_input)
        
        self.category_dropdown = QtWidgets.QComboBox()
        self.category_dropdown.addItems(["Needs", "Wants", "Savings"])
        layout.addWidget(self.category_dropdown)
        
        self.description_input = QtWidgets.QLineEdit()
        self.description_input.setPlaceholderText("Enter description")
        layout.addWidget(self.description_input)
        
        self.add_button = QtWidgets.QPushButton("Add Expense")
        self.add_button.clicked.connect(self.add_expense)
        layout.addWidget(self.add_button)
        
        self.save_button = QtWidgets.QPushButton("Save & Exit")
        self.save_button.clicked.connect(self.save_data)
        layout.addWidget(self.save_button)
        
        self.setLayout(layout)

    def add_expense(self):
        try:
            amount = float(self.amount_input.text())
            category = self.category_dropdown.currentText()
            description = self.description_input.text()
        
            if amount > self.balance:
                QtWidgets.QMessageBox.warning(self, "Error", "Not enough balance!")
                return
            
            self.expenses.append({
                "amount": amount,
                "category": category,
                "description": description
            })
            self.balance -= amount
            self.update_expense_list()
            self.balance_label.setText(f"Balance: £{self.balance}")
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Error", "Please enter a valid amount")

    def update_expense_list(self):
        self.expense_list.clear()
        for exp in self.expenses:
            self.expense_list.addItem(f"£{exp['amount']} | {exp['category']} | {exp['description']}")

    def load_data(self):
        try:
            with open("budget_data.json", "r") as file:
                data = json.load(file)
                self.income = data.get("income", 0)
                self.expenses = data.get("expenses", [])
                self.balance = data.get("balance", self.income)
        except FileNotFoundError:
            self.income, self.expenses, self.balance = 0, [], 0

    def save_data(self):
        data = {"income": self.income, "expenses": self.expenses, "balance": self.balance}
        with open("budget_data.json", "w") as file:
            json.dump(data, file, indent=4)
        QtWidgets.QMessageBox.information(self, "Saved", "Budget data saved successfully!")
        sys.exit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = BudgetTrackerApp()
    window.show()
    sys.exit(app.exec())
