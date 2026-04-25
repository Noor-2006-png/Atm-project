import utils
from datetime import datetime

def deposit_money(amount):
    utils.balance += amount
    date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    utils.transactions.append(f"{date} | Deposited: ₹{amount}")
    return "Amount deposited successfully"