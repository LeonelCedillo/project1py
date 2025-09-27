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
        # string format time: 2025-08-18 00:00:00 --> 2025-8-18
        formated_date = self.date.strftime("%Y-%m-%d")
        return f"Transaction({formated_date}, {self.tType}, {self.description}, {self.amount}, {self.balance})"