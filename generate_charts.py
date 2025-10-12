import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import get_cmap
from matplotlib.patches import Patch


def category_summary_chart(categories_dict):
    plt.figure(figsize=(8,5))  
    plt.clf()  
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
    plt.close() 


def balance_trend_chart(dates, balances):
    plt.figure(figsize=(8,5))  
    plt.clf()  
    dates = [d.strftime("%y/%m") for d in dates]
    plt.plot(dates, balances, marker='o')
    plt.xlabel("Date (YY/MM)")
    plt.ylabel("Balance $")
    plt.title("Balance Trend")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("balance_trend.png")
    plt.close() 


def monthly_cashflow_chart(monthly_cashflow_dict):
    plt.figure(figsize=(8,5))  
    plt.clf()  
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
    plt.close() 


def top_expenses_chart(expenses_list_dict):
    plt.figure(figsize=(8,5))  
    plt.clf()  
    dates = [e["date"] for e in expenses_list_dict]
    cats = [e["category"] for e in expenses_list_dict]
    subcats = [e["subcategory"] for e in expenses_list_dict]
    amounts = [abs(e["amount"]) for e in expenses_list_dict]

    # A color to each unique category
    unique_categories = list(set(cats))
    cmap = get_cmap("tab10")
    color_map = {cat: cmap(i) for i, cat in enumerate(unique_categories)}
    colors = [color_map[cat] for cat in cats]
    
    # Horizontal bar chart
    y_pos = range(len(dates))
    bars = plt.barh(y_pos, amounts, color=colors)
    plt.xlabel("Amount ($)")
    plt.title("Top Expenses")
    plt.gca().invert_yaxis()  # largest on top
    # Set y-axis labels to dates
    plt.yticks(y_pos, dates)
    
    # Amounts labels on bars
    for bar, subcat, width in zip(bars, subcats, amounts):
        plt.text(6, bar.get_y() + bar.get_height(), subcat, 
             ha="left", va="bottom", color="white")
        plt.text(width - 50, bar.get_y() + bar.get_height()/2, f"${width:.2f}",
             ha="right", va="center", color="white", fontweight="bold")
    
    # Legend
    legend_elements = [Patch(facecolor=color_map[cat], label=cat) for cat in unique_categories]
    plt.legend(handles=legend_elements, title="Category", bbox_to_anchor=(1,0.5), loc="center left")
    
    # Save chart
    plt.tight_layout()
    plt.savefig("top_expenses.png")
    plt.close() 


def subcategories_chart(cat_subcat):
    plt.clf()
    print(cat_subcat)
    for category, subdata in cat_subcat.items():
        title = category.name
        labels = list(subdata.keys())
        values = [abs(v) for v in subdata.values()]
        plt.figure()
        plt.pie(values, labels=labels, autopct="%1.1f%%")
        plt.title(title)

        # Save chart
        plt.tight_layout()
        plt.savefig(f"{title}_pie.png")
        plt.close() 

