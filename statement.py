import utils

def show_statement():
    if not utils.transactions:
        return ["No transactions yet"]
    return utils.transactions