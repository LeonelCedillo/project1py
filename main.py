from transac_obj import get_transaction_objects
from transaction import Category

transactions = get_transaction_objects()
# for t in transactions:
#     print(t)

def format_amount(amount):
    if amount < 0:
        return f"-${abs(amount):.2f}"
    return f"${abs(amount):.2f}"

def get_initial_balance(transactions):
    return transactions[0].balance - transactions[0].amount

def get_final_balance(transactions):
    return transactions[len(transactions) - 1].balance


def summarize_by_category(transactions):
    categories = {c.name: 0 for c in Category}
    for t in transactions: 
        if t.category in categories:
            categories[t.category] += t.amount
    print("Category Summary:")
    print("-----------------")
    for key, val in categories.items(): 
        if val != 0: 
            print(f"{key}: {format_amount(val)}")
    init_balance = get_initial_balance(transactions)
    fin_balance = get_final_balance(transactions)
    print("")
    print(f"Initial Balance: {format_amount(init_balance)}")
    print(f"Final Balance: {format_amount(fin_balance)}")


def summarize_by_month(transactions):
    months = {}
    for t in transactions:
        month = t.date.strftime("%B")
        curr_amount = round(months.get(month, 0) + t.amount, 2) # two zeroes instead of one ***
        months[month] = curr_amount

    print("Monthly Cashflow:")
    print("-----------------")
    for key, val in months.items():
        print(f"{key}:  ${val}")



summarize_by_month(transactions)

# Monthly Cashflow:
# -----------------
# January 2025: Inflow: $6000.00, Outflow: $3500.00, Net: $2500.00
# February 2025: Inflow: $4000.00, Outflow: $3300.00, Net: $700.00
