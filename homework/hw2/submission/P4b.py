#!/usr/bin/env python3
# File       : P3.py
# Description: Bank account withdraw: Part B
# Copyright 2022 Harvard University. All Rights Reserved.

def atm_visit(initial_balance):
   
    def make_withdraw(amount):
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

#Explanation
explanation = """
In this version of the code, I added a line that updated the initial balance to be the final balance after the withdraw had occurred. However, now this results in an UnboundLocal Error: local variable 'initial_balance' referenced before assignment. 
After reviewing python documentation provided, I think the issue is that this updated initial balance is defined in the nested function, which means its scope only extends to that function block. However, the outermost function, atm_visit, accepts the initial_value as an argument. Once inital_balance is captured by the inner function, it can't be changed, as we learned when talking about data encapsulation.  
"""
print(explanation)
