from datetime import datetime

balance = 1000
transactions = []
PIN = "1234"   # default PIN


def verify_pin():
    attempts = 3
    while attempts > 0:
        entered = input("Enter your PIN: ")
        if entered == PIN:
            return True
        else:
            attempts -= 1
            print(f"Wrong PIN! Attempts left: {attempts}")
    return False