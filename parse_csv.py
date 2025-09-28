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

    
def add_category(txn):
    desc = txn[2].lower()
    txnType = txn[1]
    rules = {
        ("@ atm", Type.DEBIT): (Category.CASH_WITHDRAWAL, "ATM"),
        ("@ atm", Type.CREDIT): (Category.DEPOSIT, "ATM"),
        ("credit crd", Type.DEBIT): (Category.PAYMENT, "Credit Card"),
        ("credit crd", Type.CREDIT): (Category.DEPOSIT, "Credit Card"),
        ("robinhood", Type.DEBIT): (Category.INVESTMENT, "Robinhood"),
        ("robinhood", Type.CREDIT): (Category.DEPOSIT, "Robinhood"),
        ("fidelity", Type.DEBIT): (Category.INVESTMENT, "Fidelity"),
        ("fidelity", Type.CREDIT): (Category.DEPOSIT, "Fidelity"),
        ("zelle", Type.DEBIT): (Category.PAYMENT, "Zelle"),
        ("zelle", Type.CREDIT): (Category.DEPOSIT, "Zelle"),
        ("jp morgan chase", Type.DEBIT): (Category.OTHER, "JP Morgan Chase"),
        ("jp morgan chase", Type.CREDIT): (Category.DEPOSIT, "JP Morgan Chase"),
        (" ucla ", Type.DEBIT): (Category.PAYMENT, "UCLA"),
        (" ucla ", Type.CREDIT): (Category.DEPOSIT, "UCLA"),
        (" nyu ", Type.DEBIT): (Category.PAYMENT, "NYU"),
        (" nyu ", Type.CREDIT): (Category.DEPOSIT, "NYU"),
        (" csu ", Type.DEBIT): (Category.PAYMENT, "CSU"),
        (" csu ", Type.CREDIT): (Category.DEPOSIT, "CSU")
    }
    for (keywork, t_type), (cat, subcat) in rules.items():
        if keywork in desc and t_type == txnType:
            txn.append(cat)
            txn.append(subcat)
            return txn
    txn.append(Category.OTHER)
    txn.append("unknown")
    return txn


