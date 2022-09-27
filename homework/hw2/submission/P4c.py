#!/usr/bin/env python3
# File       : P3.py
# Description: Bank account withdraw: Part C
# Copyright 2022 Harvard University. All Rights Reserved.
def atm_visit(initial_balance):
   
    def make_withdraw(amount):
        nonlocal initial_balance
        if amount > initial_balance:
            raise ValueError(f"Amount ${amount} exceeds balance ${initial_balance}.")
        else:
            # set new balance
            final_balance = initial_balance - amount
            final_balance = float(final_balance)
            initial_balance = final_balance
            return final_balance    
    return make_withdraw

# Test
# test values
initial_balance = 100
withdraw1 = 10
withdraw2 = 20
# test script
money_left = atm_visit(initial_balance)
print(f"${money_left(withdraw1)}")
print(f"${money_left(withdraw2)}")
