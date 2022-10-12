#!/usr/bin/env python3
# File       : P4.py
# Description: Bank account revisited
# Copyright 2022 Harvard University. All Rights Reserved.

# So this is my 26 tests passed late day updated version, based on max bank.py (and P4.py) (and late day P4.py) (and 25 tests version)

from enum import Enum

class Account(Enum):
    '''
    Simple enumeration
    See: https://stackoverflow.com/questions/22586895/python-enum-when-and-where-to-use
    '''
    SAVINGS = 1
    CHECKING = 2

class BankAccount():
    '''Class for creating a bank account. Allows for deposits and withdrawals.'''
    
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
        if amount < float(0):
            raise ValueError("Withdrawal amount can't be negative")    
        self.balance = self.balance - amount
        return self.balance        

    def deposit(self, amount: float):  
        if amount < float(0):
            raise ValueError("Deposit amount can't be negative")   
        self.balance = self.balance + amount
        return self.balance                
        
           
        
        
        
        
class Customer():

    def __init__(self, name):
        self.name = name
        self.saving_account = None
        self.checking_account = None
 
    def __str__(self):
        if self.saving_account is None and self.checking_account is None:
            return f"{self.name} has no active accounts"
        elif self.saving_account is None:
            return f"{self.name} has a {self.checking_account.__str__()}"
        elif self.checking_account is None:
            return f"{self.name} has a {self.saving_account.__str__()}"
        else:
            return f"{self.name} has a {self.saving_account.__str__()} and a {self.checking_account.__str__()}"

    def __len__(self):
        if self.checking_account is None and self.saving_account is None:
            return 0
        if self.checking_account is None and self.saving_account is not None:
            return 1
        if self.checking_account is not None and self.saving_account is None:
            return 1
        if self.checking_account is not Nonte and self.saving_account is not None:
            return 2
    
    def add_account(self, account_type: Account):
        
        if account_type == Account.CHECKING:
            if self.checking_account == None:
                self.checking_account = BankAccount(account_type)
                
            else:
                raise Exception("Can only have one checking account")
        else:
            if self.saving_account == None:
                self.saving_account = BankAccount(account_type)              
            else:
                raise Exception("Can only have one savings account")

    def get_balance(self, account_type: Account):
        if account_type == Account.SAVINGS:
            if self.saving_account is None:
                raise Exception("This account does not exist")
            else:
                return self.saving_account.get_balance()
        if account_type == Account.CHECKING:
            if self.checking_account is None:
                raise Exception("This account does not exist")
            else:
                return self.checking_account.get_balance()

    def deposit(self, account_type: Account, amount: float):
        if account_type == Account.SAVINGS:
            if self.saving_account is None:
                raise Exception("This account does not exist")
            else:
                return self.saving_account.deposit(amount)
        if account_type == Account.CHECKING:
            if self.checking_account is None:
                raise Exception("This account does not exist")
            else:
                return self.checking_account.deposit(amount)

    def withdraw(self, account_type: Account, amount: float):
        if account_type == Account.CHECKING:
            if self.checking_account is None:
                raise Exxception("This account does not exist")
            return self.checking_account.withdraw(amount)
        elif account_type == Account.SAVINGS:
            if self.saving_account is None:
                raise Exception("This account does not exist")
            return self.saving_account.withdraw(amount)
             
            
            
            
            
            
def ATMSession(user: Customer):
    if type(user) is not Customer:
        raise Exception('User is not type customer')
    def interface():
        while True:
            main_screen = input("1) Exit \n2) Create Account \n3) Check Balance \n4) Deposit \n5 Withdraw \nEnd")
            selection = int(main_screen)

            if selection not in [1,2,3,4,5]:
                raise ValueError("Invalid Selection.")

            if selection == 1:
                print("End of Session")
                return 0

            if selection in [2,3,4,5]:
                sub_screen = input("1) Checking \n2) Savings \nChoose Account:")
                if int(sub_screen) == 1:
                    account_type = Account.CHECKING
                elif int(sub_screen) == 2:
                    account_type = Account.SAVINGS
                elif int(sub_screen) not in [1,2]:
                    raise ValueError("Invalid Selection")

                if selection == 2:
                    user.add_account(account_type)

                if selection == 3:
                    print(user)

                if selection == 4:
                    deposit_unit = input("Enter Deposit Amount:")
                    deposit_amount = float(deposit_input)
                    user.deposit(account_type, deposit_amount)

                if selection == 5:
                    withdraw_input = input("Enter Withdraw Amount")
                    withdraw_amount = float(withdraw_input)
                    user.withdraw(account_type, withdraw_amount)
            else:
                raise Exception("Invalid Selection")
    return interface

