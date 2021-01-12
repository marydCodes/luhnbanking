# Write your code here
import random
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS card(id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0 )')


def menu():
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")
    choice = input()

    if choice == '1':
        create_account()
        menu()
    elif choice == '2':
        log_in()
        menu()
    elif choice == '0':
        exit()
    else:
        print('Select from options 0,1,2')
        menu()


def create_account():
    print('Your card has been created')
    card_one = random.randint(400000000000000, 400000999999999)
    card = csalg(card_one)
    pin = create_pin()
    print('Your card number:')
    print(card)
    print('Your card PIN:')
    print(pin)
    cur.execute('INSERT INTO card(number, pin) VALUES(?, ?)', (card, pin))
    conn.commit()


def create_pin():
    pin = str(random.randint(0, 9))
    for i in range(3):
        pin = pin + str(random.randint(0, 9))
    return pin


def log_in():
    print('Enter your card number:')
    cardin = int(input())
    print('Enter your PIN:')
    pinin = input()
    cur.execute('SELECT number, pin FROM card WHERE number =:number', {"number": cardin})
    result = cur.fetchone()
    if type(result) != tuple:
        print('Wrong card number or PIN!')
        menu()
    elif result[1] != pinin:
        print('Wrong card number or PIN!')
        menu()
    else:
        if result[1] == pinin:
            print('You have successfully logged in!')
            logged_in()


def logged_in():
    print('1. Balance')
    print('2. Log out')
    print('0. Exit')
    choice = input()
    if choice == '1':
        print('Balance: 0')
        logged_in()
    elif choice == '2':
        print('You have successfully logged out!')
        menu()
    elif choice == '0':
        print('Bye!')
        exit()
    else:
        logged_in()


def csalg(cardin):
    cardlist = [int(x) for x in str(cardin)]
    algcheck = []
    count = 1
    for x in cardlist:
        if count % 2 != 0:
            if (x * 2) > 9:
                algcheck.append((x * 2) - 9)
            else:
                algcheck.append(x * 2)
        else:
            algcheck.append(x)
        count += 1
    lastdig = int(str(sum(algcheck))[-1])
    if lastdig == 0:
        algcheck.append(lastdig)
    else:
        algcheck.append((10 - lastdig))

    finalcard = ''
    cardlist.append(algcheck[-1])
    return int(finalcard.join(str(z) for z in cardlist))


menu()