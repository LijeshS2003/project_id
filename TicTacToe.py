# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 20:37:11 2023

@author: Lijesh.S
"""


import numpy
b=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1='X'
p2='O'

def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if b[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol,'won')
            return True
    return False

def check_cols(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if b[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol,'won')
            return True
    return False
                        
def check_diagonals(symbol):
    if b[0][2]==b[1][1] and b[1][1]==b[2][0] and b[1][1]==symbol:
            print(symbol,'won')
            return True
    if b[0][0]==b[1][1] and b[1][1]==b[2][2] and b[1][1]==symbol:
            print(symbol,'won')
            return True
    return False

def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)

def place(symbol):
    print(numpy.matrix(b))
    while(1):
        
         row=int(input('Enter row -1 or 2 or 3:'))
         col=int(input('Enter col -1 or 2 or 3:'))
         if row>0 and row<4 and col>0 and col<4 and b[row-1][col-1]=='-':
            break
         else:
            print("Invalid Input, Please enter again")
    b[row-1][col-1]=symbol
def play():
    for turn in range(9):
        if turn%2==0:
            print("X turn")
            place(p1)
            if won(p1):
                 break
        else:
            print('0 turn')
            place(p2)
            if won(p2):
                break
        if not(won(p1)) and not(won(p2)):
            print("Draw")
play()