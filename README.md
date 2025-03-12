# Python Budget Tracker 💰📊

## Overview
A simple and efficient **command-line budget tracker** to help you manage your monthly finances by categorizing expenses and tracking your balance.

## Features
✅ **Track Income & Expenses** – Log income and categorize expenses into Needs, Wants, and Savings.  
✅ **View Spending History** – See past transactions with timestamps.  
✅ **Monthly Budget Summary** – Get a breakdown of spending and available balance.  
✅ **Auto-Save & Load Data** – Persist data using JSON for future reference.  
✅ **User-Friendly CLI Interface** – Simple input system for easy tracking.  

## Installation
### Prerequisites
- Python 3.x installed on your system

### Clone the Repository
```sh
git clone https://github.com/yourusername/budget-tracker.git
cd budget-tracker
```

### Run the Tracker
```sh
python budget_tracker.py
```

## Usage
1. **Enter your monthly income** at the start.
2. **Log expenses** by entering the amount, category (Needs, Wants, or Savings), and description.
3. **View your budget summary** anytime to see spending patterns.
4. **Save & Exit** to store data automatically for future sessions.

## Example
```
Enter your monthly income: £2000

Options: 1) Add Expense  2) View Expenses  3) Summary  4) Save & Exit
Choose an option: 1
Enter expense amount: £50
Enter category (Needs, Wants, Savings): Wants
Enter description: Gaming Subscription
Added expense: £50 for Gaming Subscription under Wants
```

## File Structure
```
📁 budget-tracker
 ├── budget_tracker.py  # Main Python script
 ├── budget_data.json   # Auto-generated storage file
 ├── README.md          # Project documentation
```

## Future Enhancements
🔹 Graphical dashboard for spending visualization  
🔹 Automatic categorization using AI  
🔹 CSV/Excel export for advanced analysis  

## License
This project is open-source and available under the MIT License.

---
📢 **Contributions are welcome!** Feel free to fork, modify, and enhance the project.

