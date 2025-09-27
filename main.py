from transaction import Type, Transaction
from datetime import datetime

# raw row:
# "Date","ReferenceNo.","Type","Description","Debit","Credit","CheckNumber","Balance"

def filter_line(line):
    txn = [x.strip('"') for x in line.split(",")]
    tranType = []
    if txn[2] == "DEBIT":
        tranType.append(txn[4])
    elif txn[2] == "CREDIT":
        tranType.append(txn[5])
    txn = [txn[0]] + txn[2:4] + tranType + [txn[7].strip('"\n')]
    return txn


def normalize_transaction(txn):
    description = t[2]
    if not t[3] or not t[4]: 
        raise ValueError(f"Missing amount or balance in row: {t}")
    amount = float(t[3])
    balance = float(t[4])
    tType = None

    if t[1] == "DEBIT": 
        tType = Type.DEBIT
        if amount > 0: 
            amount = -amount
    elif t[1] == "CREDIT":
        tType = Type.CREDIT
        if amount < 0:
            amount = -amount
    try: 
        # string parse time: 8/18/2025 --> 2025-08-18 00:00:00
        date_obj = datetime.strptime(t[0], "%m/%d/%Y") 
        # string format time: 2025-08-18 00:00:00 --> 2025-8-18
        formated_date = date_obj.strftime("%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Invalid date format in row: {t}")

    normalized_transactions.append([date_obj, tType, description, amount, balance])


transactions = []
with open("export.csv") as file:
    next(file)
    for line in file:
        txn = filter_line(line)  # To: ["Date","Type","Description","Amount","Balance"]
        if float(txn[3]) == 0.0:
            continue
        normalized_txn = normalize_transaction(txn) # To: [Date obj, Type type, "Description", Amount float, Balance float]
        
        # working here ***


    

# Create Transaction Objecs:
# Date obj, Type type, "Description", Amount float, Balance float
# to: 
# Transaction(date, type, description, amount, balance)
transaction_objs = []
for t in transactions: 
    tran = Transaction(t[0], t[1], t[2], t[3], t[4])
    transaction_objs.append(tran)
for t in transaction_objs:
    print(t)

