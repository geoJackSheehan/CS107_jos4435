#!/usr/bin/env python3
# File       : P3.py
# Description: Bank account withdraw: Part A
# Copyright 2022 Harvard University. All Rights Reserved.
def atm_visit(initial_balance):
   
    def make_withdraw(amount):
        if amount > initial_balance:
            raise ValueError(f"Amount ${amount} exceeds balance ${initial_balance}.")
        else:
            # set new balance
            final_balance = initial_balance - amount
            final_balance = float(final_balance)
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

#Explanation
explanation = """
This behavior is not correct. After one withdraw, the initial balance is not updated to the final balance. Therefore, every subsequent withdraw will use the very first initial balance, regardless of how many withdraws have already taken place. In this test, the result of withdraw1 is correct, because no withdraws have yet taken place. However, withdraw2 is incorrect, because it is not updated to reflect the fact that withdraw1 occurred.
"""
print(explanation)
