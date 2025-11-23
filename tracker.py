# Minimal expense tracker implementing Feature 3 (Add New Expense) and Feature 4 (View Expenses)

import csv
from datetime import datetime
from pathlib import Path

BASEDIR = Path(__file__).parent
BALANCEFILE = BASEDIR / "balance.txt"
EXPREFIX = "expenses_"

def readbal():
    try:
        text = BALANCEFILE.read_text().strip()
        return float(text)
    except FileNotFoundError:
        BALANCEFILE.write_text("0.00\n")
        return 0.0
    except ValueError:
        print("Warning: balance file malformed, resetting to 0.00")
        BALANCEFILE.write_text("0.00\n")
        return 0.0

def writebal(newbal):
    BALANCEFILE.write_text(f"{newbal:.2f}\n")

def header():
    bal = readbal()
    print(f"\nAvailable balance: {bal:.2f}\n")

def getdate():
    while True:
        s = input("Enter date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(s, "%Y-%m-%d")
            return s
        except ValueError:
            print("Invalid format. Example: 2025-11-07")

def getitem():
    while True:
        it = input("Item name: ").strip()
        if it:
            return it
        print("Item name cannot be empty.")

def getamount():
    while True:
        s = input("Amount paid: ").strip()
        try:
            a = float(s)
            if a <= 0:
                print("Amount must be positive.")
                continue
            return round(a, 2)
        except ValueError:
            print("Enter a valid number (e.g. 12.50)")

def expfile(datestr):
    return BASEDIR / f"{EXPREFIX}{datestr}.txt"

def nextid(fpath):
    if not fpath.exists():
        return 1
    try:
        with fpath.open(newline='', encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = list(reader)
            if not rows:
                return 1
            last = rows[-1]
            return int(last[0]) + 1
    except (IndexError, ValueError, UnicodeDecodeError) as e:
        print("Warning: corrupt expense file, starting ids at 1:", e)
        return 1

def add():
    header()
    datestr = getdate()
    it = getitem()
    amt = getamount()

    print("\nYou entered:")
    print(f" Date:   {datestr}")
    print(f" Item:   {it}")
    print(f" Amount: {amt:.2f}")
    conf = input("Save this expense? (y/n): ").strip().lower()
    if conf != 'y':
        print("Cancelled. Returning to menu.")
        return

    bal = readbal()
    if amt > bal:
        print("Insufficient balance! Cannot save expense.")
        return

    fpath = expfile(datestr)
    eid = nextid(fpath)
    recorded = datetime.now().isoformat(sep=' ', timespec='seconds')

    needhdr = not fpath.exists()
    with fpath.open("a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        if needhdr:
            writer.writerow(["id", "item", "amount", "recorded_at"])
        writer.writerow([eid, it, f"{amt:.2f}", recorded])

    newbal = round(bal - amt, 2)
    writebal(newbal)

    print(f"Expense saved. Remaining balance: {newbal:.2f}")

def findfiles():
    return sorted(BASEDIR.glob(f"{EXPREFIX}*.txt"))

def searchitem():
    q = input("Enter item name (substring, case-insensitive): ").strip().lower()
    if not q:
        print("Empty query.")
        return
    files = findfiles()
    found = False
    for fp in files:
        with fp.open(newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if q in row.get("item", "").lower():
                    print(f"{fp.name} | id={row.get('id')} | item={row.get('item')} | amount={row.get('amount')} | recorded_at={row.get('recorded_at')}")
                    found = True
    if not found:
        print("No matching expenses found.")

def searchamount():
    s = input("Enter amount to search (exact match): ").strip()
    try:
        target = float(s)
    except ValueError:
        print("Invalid number.")
        return
    files = findfiles()
    found = False
    for fp in files:
        with fp.open(newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    a = float(row.get("amount", "0"))
                    if abs(a - target) < 0.005:
                        print(f"{fp.name} | id={row.get('id')} | item={row.get('item')} | amount={row.get('amount')} | recorded_at={row.get('recorded_at')}")
                        found = True
                except Exception:
                    continue
    if not found:
        print("No matching expenses found.")

def viewmenu():
    while True:
        print("\nView Expenses - Search options:")
        print("1. Search by item name")
        print("2. Search by amount")
        print("3. Back to main menu")
        choice = input("Choice: ").strip()
        if choice == "1":
            searchitem()
        elif choice == "2":
            searchamount()
        elif choice == "3":
            return
        else:
            print("Invalid choice.")

def viewbal():
    bal = readbal()
    print(f"\nCurrent balance: {bal:.2f}\n")
    input("Press Enter to return to menu...")

def menu():
    while True:
        header()
        print("Main Menu:")
        print("1. View Balance")
        print("2. Add New Expense")
        print("3. View Expenses")
        print("4. Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            viewbal()
        elif choice == "2":
            add()
        elif choice == "3":
            viewmenu()
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()