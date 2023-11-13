import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
temp = 99999
final_temp = 0
n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    if(abs(t) < temp):
        temp = abs(t)
        final_temp = t
    elif(abs(t) == temp):
        temp = abs(t)
        if(final_temp == t):
            pass
        else:
            final_temp = abs(t)
    

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(final_temp)
