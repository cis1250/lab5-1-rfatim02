#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def abc():
    while True:
        user_number = int(input("Enter a positive number of a term for the Fibonacci sequence"))
        if user_number <= 0:
            print("invalid number. Enter a positive number")
        else: 
            calculation(user_number)
            
def calculation(user_number): 
        num1 = 0
        num2 = 1
        for i in range(user_number):
            total = num1 + num2
            print(num1)
            #print("")
            num1 = num2 
            num2 = total
abc()
