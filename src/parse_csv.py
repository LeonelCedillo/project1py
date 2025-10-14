from transaction import Type, Category, Transaction
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

    return [date_obj, tType, description, amount, balance]

    
def add_category(txn, rules):
    desc = txn[2].lower()
    txnType = txn[1].name
    for keyword, rule in rules[txnType].items():
        if keyword in desc:
            match (rule["category"]):
                case "PAYMENT":
                    cat = Category.PAYMENT
                case "TRANSFER":
                    cat = Category.TRANSFER
                case "INVESTMENT":
                    cat = Category.INVESTMENT
                case "CASH_WITHDRAWAL":
                    cat = Category.CASH_WITHDRAWAL
                case "DEPOSIT":
                    cat = Category.DEPOSIT
                case "OTHER":
                    cat = Category.OTHER
            txn.append(cat)
            txn.append(rule["subcategory"])
            return txn
    txn.append(Category.OTHER)
    txn.append("unknown")
    return txn
