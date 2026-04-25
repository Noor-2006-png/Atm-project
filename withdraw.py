import utils
from datetime import datetime

def withdraw_money(amount):
    if amount <= utils.balance:
        utils.balance -= amount
        date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        utils.transactions.append(f"{date} | Withdrawn: ₹{amount}")
        return "Withdrawal successful"
    else:
        return "Insufficient balance"