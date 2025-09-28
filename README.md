# project1py
First personal project with python


### Sample `rules.json`

This file defines keyword-based rules for categorizing transactions.  
Each keyword can have different categories for `DEBIT` and `CREDIT`.

```json
{
  "KEYWORDS": ["@ atm", "zelle"],
  "DEBIT": {
    "@ atm": {"category": "CASH_WITHDRAWAL", "subcategory": "ATM"},
    "zelle": {"category": "PAYMENT", "subcategory": "Zelle"}
  },
  "CREDIT": {
    "@ atm": {"category": "DEPOSIT", "subcategory": "ATM"},
    "zelle": {"category": "DEPOSIT", "subcategory": "Zelle"}
  }
}
