from enum import Enum


class Type(Enum):
    DEBIT = "withdrawal"
    CREDIT = "deposit"


class Transaction:
    def __init__(self, date, tType, description, amount, balance):
        self.date = date
        self.tType = tType
        self.description = description
        self.amount = amount
        self.balance = balance

    
    def __repr__(self):
        return f"Transaction({self.date}, {self.tType}, {self.description}, {self.amount}, {self.balance})"