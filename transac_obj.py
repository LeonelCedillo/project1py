from parse_csv import filter_line, normalize_transaction, add_category
from transaction import Transaction
import json

# raw row:
# "Date","ReferenceNo.","Type","Description","Debit","Credit","CheckNumber","Balance"

def get_transaction_objects():
    with open("rules.json", "r") as f:
        rules = json.load(f)
    transaction_objs = []
    prev_balance = None

    with open("export.csv") as file:
        next(file) # skip header
        for line in file:
            txn = filter_line(line)  # To: ["Date","Type","Description","Amount","Balance"]
            if float(txn[3]) == 0.0 and float(txn[4]) == 0.0:
                # print(f"Skipping row (repeated): {txn}")
                continue
            txn = normalize_transaction(txn, prev_balance)  # To: [Date obj, Type type, "Description", Amount float, Balance float]
            prev_balance = float(txn[4])
            txn = add_category(txn, rules)
            date, tType, description, amount, balance, category, subcategory = txn
            txn_obj = Transaction(date, tType, description, amount, balance, category, subcategory)
            transaction_objs.append(txn_obj)  
    return transaction_objs