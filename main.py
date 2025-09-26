from transaction import Type, Transaction
from datetime import datetime


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
        if tran[3] != "0":
            transactions.append(tran)

for t in transactions:
    date_str = t[0]
    date = datetime.
    tType = t[1]
    description = t[2]
    amount = float(t[3])
    balance = float(t[4])




# "Date","ReferenceNo.","Type","Description","Debit","Credit","CheckNumber","Balance"

# tran1 = Transaction("1/3/2025", Type.DEBIT.value, "Withdrawal @ ATMGO8 111 E SHAW etc", -400, 7681.28)
# print(tran1)
