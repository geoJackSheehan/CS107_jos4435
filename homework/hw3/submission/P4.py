#!/usr/bin/env python3
# File       : P4.py
# Description: Bank account revisited
# Copyright 2022 Harvard University. All Rights Reserved.
# Author: Jack Sheehan. Worked with Chiara Chung-Halpern

from enum import Enum

class Account(Enum):
    SAVINGS = 1
    CHECKING = 2

class BankAccount():
    def __init__(self, account_type: Account):
        self.account_type = account_type
        self.balance = float(0)

    def __str__(self):
        return (f" Account Type: {self.account_type} Account Balance: {self.balance}")

    def get_type(self):
        return self.account_type

    def get_balance(self):
        return self.balance

    def withdraw(self, amount: float):   
        if amount > self.balance:
            raise ValueError("Withdrawal amount can't be larger than balance")   
        if amount < 0:
            raise ValueError("Withdrawal amount can't be negative")    
        self.balance = self.balance - amount
        return self.balance  

    def deposit(self, amount: float):  
        if amount < 0:
            raise ValueError("Deposit amount can't be negative")   
        self.balance = self.balance + amount
        return self.balance   

class Customer():
    def __init__(self, name):
        super(Customer).__init__()
        self.name = str(name)
        self.saving = None
        self.checking = None

    def __str__(self):
        return (f"Customer name: {self.name} Number of valid accounts: {self.__len__()}Amount in savings: {str(self.saving)} Amount in checking: {str(self.checking)}")

    def __len__(self):
        account = 0
        if self.saving:
            account += 1
        if self.checking:
            account += 1
        return account

    def add_account(self, account_type: Account):
        if account_type.name == 'SAVINGS':
            if not(self.saving):
                self.saving = BankAccount(account_type)
            else:
                raise ValueError('Can only have one savings account')
        elif account_type.name == 'CHECKING':
            if not(self.checking):
                self.checking = BankAccount(account_type)
            else:
                raise ValueError('Can only have one checking account')
        else:
            raise ValueError('Account input error')

    def get_balance(self, account_type: Account):
        if account_type.name == 'SAVINGS':
            if self.saving:
                print(self.saving.get_balance())
                return self.saving.get_balance()
            else:
                raise ValueError('This account does not exist')
        if account_type.name == 'CHECKING':
            if self.checking:
                print(self.checking.get_balance())
                return self.checking.get_balance()
            else:
                raise ValueError('This account does not exist')
        else:
            raise ValueError('Account input error')

    def deposit(self, account_type: Account, amount: float):
        if account_type.name == 'SAVINGS':
            saving_account = self.saving
            if saving_account:
                return saving_account.deposit(amount)
            else:
                raise ValueError('This account does not exist')
        elif account_type.name == 'CHECKING':
            checking_account = self.checking
            if checking_account:
                return checking_account.deposit(amount)
            else:
                raise ValueError('This account does not exist')
        else:
            raise ValueError('Account input error')

    def withdraw(self, account_type: Account, amount: float):
        if account_type.name == 'SAVINGS':
            saving_account = self.saving
            if saving_account:
                return saving_account.withdraw(amount)
            else:
                raise ValueError('This account does not exist')
        if account_type.name == 'CHECKING':
            checking_account = self.checking
            if checking_account:
                return checking_account.withdraw(amount)
            else:
                raise ValueError('This account does not exist')
        else:
            raise ValueError('Account input error')

def ATMSession(user: Customer):
    if type(user) is not Customer:
        raise ValueError('User is not type customer')

    def interactive_component():
        option = input("1) Exit \n2) Create Account \n3) Check Balance \n4) Deposit \n5 Withdraw")

        while option is not '1':
            if option is '2':
                choose_account = input("1) Checking \n2) Savings")
                if choose_account == '1':
                    user.add_account(Account(2))
                elif choose_account == '2':
                    user.add_account(Account(1))
                else:
                    raise ValueError('Invalid option')
            elif option is '3':
                choose_account = input("1) Checking \n2) Savings")
                if choose_account == '1':
                    user.get_balance(Account(2))
                elif choose_account == '2':
                    user.get_balance(Account(1))
                else:
                    raise ValueError('Invalid option')
            elif option is '4':
                choose_account = input("1) Checking \n2) Savings")
                if choose_account == '1':
                    amount = input('Enter amount:')
                    try:
                        amount = float(amount)
                    except:
                        raise ValueError('Invalid amount')
                    user.deposit(Account(2), amount)
                elif choose_account == '2':
                    amount = input('Enter amount:')
                    try:
                        amount = float(amount)
                    except:
                        raise ValueError('Invalid amount')
                    user.deposit(Account(1), amount)
                else:
                    raise ValueError('Invalid option')
            elif option is '5':
                choose_account = input("1) Checking \n2) Savings")
                if choose_account == '1':
                    amount = input('Enter amount:')
                    try:
                        amount = float(amount)
                    except:
                        raise ValueError('Invalid amount')
                    user.withdraw(Account(2), amount)
                elif choose_account == '2':
                    amount = input('Enter Amount:')
                    try:
                        amount = float(amount)
                    except:
                        raise ValueError('Invalid amount')
                    user.withdraw(Account(1), amount)
                else:
                    raise ValueError('Invalid option')
            else:
                raise ValueError('Invalid option')

            option = input("1) Exit \n2) Create Account \n3) Check Balance \n4) Deposit \n5 Withdraw")
        return 0
    return interactive_component
