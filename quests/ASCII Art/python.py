import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# def info(message: str):
#     print(message, file=sys.stderr, flush=True)


l = int(input())
h = int(input())
t = input()
for i in range(h):
    message= ""
    row = input()
    for let in t:
        if(ord(let)>=65 and ord(let)<=90):
            message+= row[(ord(let) - 65)*l: (ord(let) - 65)*l + l]
        elif(ord(let)>=97 and ord(let)<=122):
            message+= row[(ord(let) - 97)*l: (ord(let) - 97)*l + l]
        else:
            message+= row[len(row) - l: len(row)]
    print(message)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


