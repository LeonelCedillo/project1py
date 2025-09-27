from transaction import Type, Transaction
from datetime import datetime

# raw row:
# "Date","ReferenceNo.","Type","Description","Debit","Credit","CheckNumber","Balance"

def filter_line(line):
    txn = [x.strip('"') for x in line.split(",")]
    if txn[2] == "DEBIT":
        tranType = txn[4]
    elif txn[2] == "CREDIT":
        tranType = txn[5]
    txn = [txn[0]] + txn[2:4] + [tranType] + [txn[7].strip('"\n')]
    return txn


def normalize_transaction(txn, prev_balance=None):
    description = txn[2]
    if not txn[3] or not txn[4]: 
        raise ValueError(f"Missing amount or balance in row: {txn}")
    amount = float(txn[3])
    balance = float(txn[4])
    tType = None

    if txn[1] == "DEBIT": 
        tType = Type.DEBIT
        if amount > 0: 
            amount = -amount
    elif txn[1] == "CREDIT":
        tType = Type.CREDIT
        if amount < 0:
            amount = -amount
    if prev_balance != None:
        expected = round(prev_balance + amount, 2)
        if expected != round(balance, 2): 
            raise ValueError(f"Balance mismatch: expected {expected}, got {balance}")
    try: 
        # string parse time: 8/18/2025 --> 2025-08-18 00:00:00
        date_obj = datetime.strptime(txn[0], "%m/%d/%Y") 
    except ValueError:
        raise ValueError(f"Invalid date format in row: {txn}")

    return Transaction(date_obj, tType, description, amount, balance)


transaction_objs = []
prev_balance = None
with open("export.csv") as file:
    next(file) # skip header
    for line in file:
        txn = filter_line(line)  # To: ["Date","Type","Description","Amount","Balance"]
        if float(txn[3]) == 0.0 and float(txn[4]) == 0.0:
            print(f"Skipping row (zero amount): {txn}")
            continue
        txn_obj = normalize_transaction(txn, prev_balance)  # To: [Date obj, Type type, "Description", Amount float, Balance float]
        prev_balance = float(txn[4])
        transaction_objs.append(txn_obj)  # Transaction(date, type, description, amount, balance)


for t in transaction_objs:
    print(t)

