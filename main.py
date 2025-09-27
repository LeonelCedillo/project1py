from parse_csv import filter_line, normalize_transaction


transaction_objs = []
prev_balance = None
with open("export.csv") as file:
    next(file) # skip header
    for line in file:
        txn = filter_line(line)  # To: ["Date","Type","Description","Amount","Balance"]
        if float(txn[3]) == 0.0 and float(txn[4]) == 0.0:
            print(f"Skipping row (repeated): {txn}")
            continue
        txn_obj = normalize_transaction(txn, prev_balance)  # To: [Date obj, Type type, "Description", Amount float, Balance float]
        prev_balance = float(txn[4])
        transaction_objs.append(txn_obj)  # Transaction(date, type, description, amount, balance)


for t in transaction_objs:
    print(t)





# Categories: 

# Credit crd payment
# transfer to robinhood
# withdrawal from atm
# deposit: from CSU Fresno, from ZEllE, from atm, etc