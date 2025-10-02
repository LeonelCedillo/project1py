from transac_obj import get_transaction_objects
from transaction import Category


transactions = get_transaction_objects()


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
        in_flow = months.get(month, {}).get("inFlow", 0)
        out_flow = months.get(month, {}).get("outFlow", 0)
        net = months.get(month, {}).get("net", 0)
        if t.amount > 0: 
            in_flow += t.amount
        elif t.amount < 0: 
            out_flow += t.amount
        net += t.amount

        months[month] = {
            "inFlow": round(in_flow, 2), 
            "outFlow": round(out_flow, 2), 
            "net": round(net, 2)
        }

    print("Monthly Cashflow:")
    print("-----------------")
    print("          Inflow: Outflow: Net:")
    for key, val in months.items():
        inFlow = format_amount(val["inFlow"])
        outFlow = format_amount(val["outFlow"])
        net = format_amount(val["net"])
        print(f"{key}:  {inFlow}, {outFlow}, {net}")



def get_top_expenses(transactions, n=5):
    top = []
    for t in transactions:
        amt = t.amount
        if amt >= 0:
            continue
        if len(top) < n:
            top.append(t)
        else:
            max_txn = max(top, key=lambda txn: txn.amount)
            max_val = max_txn.amount
            if amt < max_val:
                top[top.index(max_txn)] = t

    sorted_expenses = sorted(top, key=lambda txn: txn.amount)
    print(f"Top {n} Expenses:")
    print("------------------")
    for t in sorted_expenses:
        amount = format_amount(t.amount)
        print(f"{t.date.date()} | {t.category} | {t.subcategory} | {amount}")


def get_balance_trend(transactions):
    print("Balance Trend:")
    print("--------------")
    for t in transactions:
        balance = format_amount(t.balance)
        print(f"{t.date.date()} | {balance}")


def sort_on_date(transactions, reverse):
    sorted_txns = list(sorted(transactions, key=lambda txn: txn.date, reverse=reverse))
    return sorted_txns


sorted_asc_transactions = sort_on_date(transactions, reverse=False)

get_balance_trend(sorted_asc_transactions)
