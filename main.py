from transac_obj import get_transaction_objects
from transaction import Category

transactions = get_transaction_objects()

# for t in transactions:
#     print(t)

def initial_balance(transactions):
    initial_balance = transactions[0].balance + transactions[0].amount
    return initial_balance


def summarize_by_category(transactions):
    categories = {c.name: 0 for c in Category}
    for t in transactions: 
        if t.category in categories.keys():
            categories[t.category] += t.amount

    print("Category Summary:")
    print("-----------------")
    for key, val in categories.items(): 
        val = round(float(val), 2)
        print(f"{key}: {val}")

    final_balance = transactions[len(transactions) - 1].balance
    print("")
    print(initial_balance)
    print(final_balance)




category_summary = summarize_by_category(transactions)
print(category_summary)