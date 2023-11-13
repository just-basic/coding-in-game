import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
start_x = initial_tx
start_y = initial_ty
# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    message: str = ""
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    if(start_y < light_y):
        message += "S"
        start_y += 1
    elif(start_y > light_y):
        message += "N"
        start_y -= 1
    else:
        pass
    if(start_x < light_x ):
        message += "E"
        start_x += 1
    elif(start_x > light_x):
        message += "W"
        start_x -= 1
    else:
        pass

        
    print("Debug: "+ str(start_x) + str(start_y), file=sys.stderr, flush=True)
    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(message)
