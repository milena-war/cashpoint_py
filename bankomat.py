"""This script is a simple ATM. Lets a user do simple bank opperations"""
import sys


def check_balance(balance):
    """ Function printing the current balance"""
    print(f'Your account balance amount to {balance} PLN')


def deposit_funds(balance):
    """ Function asks the user about funds amount which wish to deposit.
    Returns balance after successful deposit"""
    deposit = int(input('Enter the amount you wish to deposit \n'))
    balance += deposit
    print(f'Your account balance is {balance} PLN')
    return balance


def withdraw_funds(balance):
    """ Function asks the user about funds amount which wish to withdraw.
     If the amount is greater than the current balance, the function
     prints an error message and returns the current balance.
     If the amount is less than the current balance, the function
     subtracts the amount from the current balance and returns the new
     balance."""
    withdraw = int(input('Enter the amount you wish to withdraw\n'))
    if withdraw > balance:
        print('Insufficient funds')
    else:
        balance -= withdraw
        print(f'Your account balance is {balance} PLN')
    return balance


def end_operation():
    """ Function ends current session"""
    print('Thank you for using our services!')
    sys.exit()


def main():
    """ Function executes the specified operation and returns the result"""
    print('Welcome to the Master Bank')
    print('Insert your card')

    password = 1793
    balance = 1500
    pin = int(input('Enter a PIN number:\n'))

    if password == pin:
        print('''
    \nMENU\n
    1 - Check account balance
    2 - Deposit
    3 - Withdraw
    4 - End operation''')

        while True:
            cashpoint = int(input('Choose an opperation: '))
            if cashpoint == 1:
                check_balance(balance)
            elif cashpoint == 2:
                balance = deposit_funds(balance)
            elif cashpoint == 3:
                balance = withdraw_funds(balance)
            elif cashpoint == 4:
                end_operation()
            else:
                print('Abnormal operation')
    else:
        print('Wrong PIN number. Please try again.')


if __name__ == "__main__":
    main()
