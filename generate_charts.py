import matplotlib.pyplot as plt
import numpy as np

def category_summary_chart(categories_dict):
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


def balance_trend_chart(dates, balances):
    dates = [d.strftime("%y/%m") for d in dates]
    plt.plot(dates, balances, marker='o')
    plt.xlabel("Date (YY/MM)")
    plt.ylabel("Balance $")
    plt.title("Balance Trend")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("balance_trend.png")


def monthly_cashflow_chart(monthly_cashflow_dict):
    months = list(monthly_cashflow_dict.keys())
    inflow = [v["inflow"] for v in monthly_cashflow_dict.values()]
    outFlow = 
    net = 
