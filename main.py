from transac_obj import get_transaction_objects
from filter_func import *
from generate_charts import *

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
category_summary_chart(categories_dict)