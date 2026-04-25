from balance import check_balance
from deposit import deposit_money
from withdraw import withdraw_money
from statement import show_statement
from utils import verify_pin

print("===== WELCOME TO ATM =====")

# PIN Authentication
if not verify_pin():
    print("Too many wrong attempts. Exiting...")
    exit()

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Statement")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance: ₹", check_balance())

    elif choice == "2":
        amt = int(input("Enter amount to deposit: "))
        print(deposit_money(amt))

    elif choice == "3":
        amt = int(input("Enter amount to withdraw: "))
        print(withdraw_money(amt))

    elif choice == "4":
        print("\n--- Transaction Statement ---")
        for t in show_statement():
            print(t)

    elif choice == "5":
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice, try again.")