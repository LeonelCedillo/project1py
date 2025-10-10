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
    months = list(m[-2:]+ " " + m[:3] for m in monthly_cashflow_dict.keys())
    inflow = [v["inFlow"] for v in monthly_cashflow_dict.values()]
    outflow = [v["outFlow"] for v in monthly_cashflow_dict.values()]
    net = [v["net"] for v in monthly_cashflow_dict.values()]

    x = np.arange(len(months))
    width = 0.25
    # plot groups bars
    plt.bar(x - width, inflow, width, label="Inflow", color="green")
    plt.bar(x, outflow, width, label="Outflow", color="red")
    plt.bar(x + width, net, width, label="Net", color="blue")
    plt.legend(title="Cashflow Type", loc="center left", bbox_to_anchor=(1, 0.5))
    # labels and formatting
    plt.xlabel("Date (YY/MM)")
    plt.ylabel("Amount ($)")
    plt.title("Monthly Cashflow")
    plt.xticks(x, months, rotation=45)
    # Save chart:
    plt.tight_layout()
    plt.savefig("monthly_cashflow.png")


def top_expenses_chart(top_expenses):
    
