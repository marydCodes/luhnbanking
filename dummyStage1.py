import random
# Write your code here
account = {}
balance = 0
while True:
    command = input('''
    1. Create an account 
    2. Log into account 
    0. Exit''')
    if command == '0':
        print('Bye!')
        break
    elif command == '1':
        cardno = int('400000'+str(random.randint(1111111111,9999999999)))
        random.seed(cardno)
        PIN = random.randint(1111,9999)
        print('Your card number:')
        print(cardno)
        print('Your card PIN:')
        print(PIN)
        account[cardno] = PIN
    elif command == '2':
        accno = int(input('Enter your card number:'))
        psd = int(input('Enter your PIN:'))
        if accno in account and account[accno] == psd:
            print('You have successfully logged in!')
            while True:
                choice = input('''
                1. Balance 
                2. Log out 
                0. Exit''')
                if choice == '1':
                    print('Balance: '+balance)
                    continue
                elif choice == '2':
                    print('You have successfully logged out!')
                    break
                else:
                    break
            if choice == '0':
                break
        else:
            print("Wrong card number or PIN!")