import random

# mii = 4
iin = "400000"
checksum = "8"
accounts = {}
balance = 0

def menu1():
    return input('''
    1. Create an account
    2. Log into account
    0. Exit
    ''')

def create_acct():
    acctid = str(random.randint(111111111, 999999999))
    cardno = iin + acctid + checksum
    random.seed(int(cardno))
    pin = str(random.randint(1111, 9999))

    return cardno, pin

def log_in():
    user = input("Enter your card number:")
    pswd = input("Enter your PIN:")
    if user in accounts and accounts[user] == pswd:
        print("You have successfully logged in!")
        return "match"
    else:
        print("Wrong card number or PIN!")
        return "no match"

def menu2():
    return input('''
    1. Balance
    2. Log out
    0. Exit
    ''')

def check_bal():
    print("Balance: ", balance)

def main():
    while True:
        choice = menu1()
        if choice == "0":
            print("Goodbye")
            break
        elif choice == "1":
            cardno, pin = create_acct()
            print("Your card number:")
            print(cardno)
            print("Your card PIN:")
            print(pin)
            accounts[cardno] = pin
        elif choice == "2":
            access = log_in()
            if access == "match":
                while True:
                    cmmd = menu2()
                    if cmmd == "1": # Balance
                        check_bal()
                        continue
                    elif cmmd == "2": # Log out
                        print("You have successfully logged out!")
                        break # returns user to menu1, OK!
                    else:
                        break
                if cmmd == "0":
                    break
        else:
            print("Invalid input")

main()