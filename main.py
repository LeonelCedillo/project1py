from transac_obj import get_transaction_objects
from transaction import Category

transactions = get_transaction_objects()

# for t in transactions:
#     print(t)

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
            print(f"{key}: {round(val, 2)}")

    init_balance = get_initial_balance(transactions)
    fin_balance = get_final_balance(transactions)
    print("")
    print(f"Initial Balance: {init_balance}")
    print(f"Final Balance: {fin_balance}")




summarize_by_category(transactions)
