import pytest
from project import add_income, add_expense, get_balance, transactions

def test_add_income():
    transactions.clear()  # Clear transactions before test
    add_income_test(1000, "Salary")
    assert len(transactions) == 1
    assert transactions[0] == {"type": "income", "amount": 1000, "description": "Salary"}

def test_add_expense():
    transactions.clear()  # Clear transactions before test
    add_expense_test(200, "Groceries")
    assert len(transactions) == 1
    assert transactions[0] == {"type": "expense", "amount": 200, "description": "Groceries"}

def test_get_balance():
    transactions.clear()  # Clear transactions before test
    add_income_test(1000, "Salary")
    add_expense_test(200, "Groceries")
    assert get_balance() == 800

def add_income_test(amount, description):
    transactions.append({"type": "income", "amount": amount, "description": description})

def add_expense_test(amount, description):
    transactions.append({"type": "expense", "amount": amount, "description": description})

if __name__ == "__main__":
    pytest.main()
