A basic command-line Personal Expense Tracker that is written in Python.
With the help of this application, you can control a balance, note the amount you spend every day, and find previous entries.

Features
View Current Balance

Automatically generates the file in case it is absent.

Checks corrupted/malformed balance values.

Add New Expense

Prompts for:

Date (YYYY-MM-DD)

Item name

Amount paid

Automatically:

Produces a file on a daily basis called expensesYYYY-MM-DD.txt.

Assigns incremental IDs

Saves the time as when the expense was recorded.

Takes away the figure off your balance.

Checks in (date format, positive amount, sufficient balance)

Search Past Expenses

Search options include:
File-Based Storage

No database required

Saved expenses in rows of CSV files under:

expenses2025-11-23.txt

Each file contains:

id, item, amount, recordedat

File Structure
yourproject/

+-- expensetracker.py # Main program (code you have provided)
+-- balance.txt # Remaining balance (generated automatically)
+-- expenses2025-11-23.txt The file contains an example of a daily expense file.

>[?] How to Run
Install Python 3

Make sure that python 3 is installed:

python3 --version

Run the program
python3 expensetracker.py

or, depending on your OS:

python expensetracker.py

How Expenses Are Saved

An expense is added each time a file is created:

expensesYYYY-MM-DD.txt

Example:

id,item,amount,recordedat
1,Milk,1.50,2025-11-23 14:32:10
2,Bread,1.20,2025-11-23 15:10:02

Searching
Search by item

Example search query:

Enter item name: milk

Output:
expenses2025-11-23.txt=1 Milk amount=1.50 recorded date=2025-11-23 14:32:10
Search by amount
Enter amount: 1.20

Input Validation

The app validates:

Correct date format
Non-empty item names
Positive numeric amounts
Adequate balance prior to incurring an expenditure.

Exit the Program

Select option 4 to quit, which is found in the main menu.
