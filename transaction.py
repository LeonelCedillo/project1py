from enum import Enum


class Type(Enum):
    DEBIT = "withdrawal"
    CREDIT = "deposit"

class Category(Enum):
    PAYMENT = "Payment" # credit card, bill, subscription, zelle
    TRANSFER = "Transfers" # checking to saving, viceversa, another bank account
    INVESTMENT = "Investments" # fidelity, robinhood
    DEPOSIT = "Deposit" # income, zelle, atm, School, 
    OTHER = "Other"


class Transaction:
    def __init__(self, date, type, description, amount, balance, category=Category.OTHER, subcategory=None):
        self.date = date
        self.type = type
        self.description = description
        self.amount = amount
        self.balance = balance
        self.category = category
        self.subcategory = subcategory

    
    def __repr__(self):
        # string format time: 2025-08-18 00:00:00 --> 2025-8-18
        formated_date = self.date.strftime("%Y-%m-%d")
        return (
            f"Transaction({formated_date}, {self.type}, {self.description}, {self.amount}, {self.balance}, {self.category}, {self.subcategory})"
        )