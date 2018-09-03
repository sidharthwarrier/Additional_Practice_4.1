# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 00:03:17 2018

@author: sidha
"""

def ispalindrome():
#Take input
    inp_str=input("Enter String to check for palindrome : ")        
#Make string caseless    
    inp_str = inp_str.casefold()
#reverse the string    
    rev_str = reversed(inp_str)
    if list(inp_str) == list(rev_str):
       print("It is palindrome")
    else:
       print("It is not palindrome")    


ispalindrome()