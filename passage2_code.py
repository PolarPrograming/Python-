#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 21:52:38 2019

@author: stanford
"""


#1
#num = random.randint(1,101)
#guess = 0
#while num != guess:
#    guess = int(input("To guess a number, please enter a number which is between 0 and 100: "))
#    if guess > num:
#        print("Guessed number is too big")
#    elif guess < num:
#        print("Guessed number is too small")
#    else:
#        print("You have got it! the number is {}".format(num))

#2
import random
num = random.randint(1,100)
#guess = 0
times = input("Please enter the maximum number of times you want to guess the number for: ")
while not times.isdigit() or int(times) <= 0:
    times = input("Please enter the maximum number of times you want to guess the number for: ")
    
for i in range(0,int(times)):
    guess = input("To guess a number, please enter a number which is between 1 and 100(inclusive): ")
    while not guess.isdigit() or int(guess) > 100 or int(guess) <= 0 : 
        print("please enter a valid number")
        guess = input("To guess a number, please enter a number which is between 1 and 100(inclusive): ")
    guess = int(guess)
    if guess > num:
        print("Guessed number is too big")
    elif guess < num:
        print("Guessed number is too small")
    else:
        #str = "shot" if i == 1 else str = "shots"
        print("You have got it! the number is {} and you have tried {} {}".format(num, i + 1, "shot" if i + 1 == 1 else "shots"))
        break
if i == int(times) - 1 and guess != num:
    print("You did not won and you have used up your chances.")
    

        
        
    