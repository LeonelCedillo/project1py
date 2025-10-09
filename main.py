from transac_obj import get_transaction_objects
from filter_func import *
import matplotlib.pyplot as plt

transactions = get_transaction_objects()
transactions = sort_on_date(transactions, reverse=False)


init_balance = get_initial_balance(transactions)
fin_balance = get_final_balance(transactions)
print(f"Initial Balance: {format_amount(init_balance)}")
print(f"Final Balance: {format_amount(fin_balance)}")
print("")

# get_balance_trend(transactions)
print("")
print("")
# summarize_by_category(transactions)
print("")
print("")
# summarize_by_month(transactions)
print("")
print("")
# get_top_expenses(transactions, 5)


categories_dict = summarize_by_category(transactions)
categories = list(str(c.name) for c in categories_dict.keys())
values = list(categories_dict.values())
colors = ['red' if v < 0 else 'blue' for v in values]

plt.bar(categories, values, color=colors)
plt.xlabel('Category')
plt.ylabel('Amount ($)')
plt.title('Category Summary')
# Save chart:
for i, val in enumerate(values):
    plt.text(i, val + (50 if val >= 0 else -50), f"${val:.2f}", ha='center', va='bottom' if val >= 0 else 'top')
plt.tight_layout()
plt.savefig("category_summary.png")