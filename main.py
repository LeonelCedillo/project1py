from src.transac_obj import get_transaction_objects
from src.filter_func import *
from src.generate_charts import *

transactions = get_transaction_objects()
transactions = sort_on_date(transactions, reverse=False)

PATH_TO_SAVE = "/data/generated_charts/"

init_balance = get_initial_balance(transactions)
fin_balance = get_final_balance(transactions)
print(f"Initial Balance: {format_amount(init_balance)}")
print(f"Final Balance: {format_amount(fin_balance)}")
print("")

# categories_dict = summarize_by_category(transactions)
# category_summary_chart(categories_dict)
# print("")

# dates, balances = get_balance_trend(transactions)
# balance_trend_chart(dates, balances)
# print("")

# monthly_cashflow_dict = summarize_by_month(transactions)
# monthly_cashflow_chart(monthly_cashflow_dict)
# print("")

# top_expenses = get_top_expenses(transactions, 5)
# top_expenses_chart(top_expenses)

subcategories = summarize_by_subcategory(transactions)
subcategories_chart(subcategories)


