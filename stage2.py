# incorporating Luhn algorithm aka Luhn formula or modulus 10

'''Checksum digit used in Luhn algorithm to verify card number is valid.
E.g. if you type your card number incorrectly by accidentally swapping two digits--when the website looks at the
number you've entered and applies the Luhn algorithm to the first 15 digits, the result won't match the 16th.
Computer knows [card] number is invalid.'''

'''Algorithm CHECKs the SUM of the digits in the card number. If the total modulus 10 == 0, then the number is valid. 
When registering in your banking system, you should generate cards with number that are checked by the Luhn 
algorithm.'''

import random

accounts = {}
balance = 0

def menu1():
    return input('''
    1. Create an account
    2. Log into account
    0. Exit
    ''')

def get_checksum(combistr):
    combi_list = list(combistr)

    # Conversion 1: multiply EVEN INDICES by 2
    combi_convert1 = []
    for idx, val in enumerate(combi_list):
        if idx % 2 == 0:
            combi_convert1.append(int(val) * 2)
        else:
            combi_convert1.append(int(val))

    # Conversion 2: subtract 9 to numbers over 9
    combi_convert2 = []
    for num in combi_convert1:
        if num < 9:
            combi_convert2.append(num)
        else:
            combi_convert2.append(num - 9)

    # Conversion 3: add all numbers
    added = sum(combi_convert2)

    # light algebra: find X; added + X = Y where Y%10 == 0
    for i in range(10):
        y = added + i
        if y % 10 == 0:
            checksum = i

    return checksum


def create_card():
    bin = "400000"
    acctid = str(random.randint(000000000, 999999999))
    combi = bin + acctid

    # generate checksum according to Luhn algorithm
    combi_list = list(combi)
    # Conversion 1: multiply EVEN INDICES by 2
    combi_convert1 = []
    for idx, val in enumerate(combi_list):
        if idx % 2 == 0:
            combi_convert1.append(int(val) * 2)
        else:
            combi_convert1.append(int(val))

    # Conversion 2: subtract 9 from numbers over 9
    combi_convert2 = []
    for num in combi_convert1:
        if num <= 9:
            combi_convert2.append(num)
        else:
            combi_convert2.append(num - 9)

    # Conversion 3: add all numbers
    added = sum(combi_convert2)

    # light algebra: find X; added + X = Y where Y%10 == 0
    for i in range(10):
        y = added + i
        if y % 10 == 0:
            checksum = i
    # checksum = str(get_checksum(combi))

    cardno = combi + str(checksum)
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
            cardno, pin = create_card()
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



