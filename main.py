from transaction import Type, Transaction
from datetime import datetime


# "Date","ReferenceNo.","Type","Description","Debit","Credit","CheckNumber","Balance"
# to:
# "Date","Type","Description","Amount","Balance"
transactions = []
with open("export.csv") as file:
    next(file)
    for line in file:
        tran = [x.strip('"') for x in line.split(",")]
        tranType = []
        if tran[2] == "DEBIT":
            tranType.append(tran[4])
        elif tran[2] == "CREDIT":
            tranType.append(tran[5])
        tran = [tran[0]] + tran[2:4] + tranType + [tran[7].strip('"\n')]
        if float(tran[3]) != 0.0:
            transactions.append(tran)


# Normalization:
# "Date","Type","Description","Amount","Balance"
# to: 
# Date obj, Type type, "Description", Amount float, Balance float
normalized_transactions = []
for t in transactions:
    description = t[2]
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
    
    # string parse time: 8/18/2025 --> 2025-08-18 00:00:00
    date_obj = datetime.strptime(t[0], "%m/%d/%Y") 
    # string format time: 2025-08-18 00:00:00 --> 2025-8-18
    formated_date = date_obj.strftime("%Y-%m-%d")

    normalized_transactions.append([date_obj, tType, description, amount, balance])


# Create Transaction Objecs:
# Date obj, Type type, "Description", Amount float, Balance float
# to: 
# Transaction(date, type, description, amount, balance)
transaction_objs = []
for t in normalized_transactions: 
    tran = Transaction(t[0], t[1], t[2], t[3], t[4])
    transaction_objs.append(tran)
for t in transaction_objs:
    print(t)

