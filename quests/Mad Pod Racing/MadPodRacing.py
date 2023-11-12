# 1st LEVEL
import sys
import math

# This code automatically collects game data in an infinite loop.
# It uses the standard input to place data into the game variables such as x and y.
# YOU DO NOT NEED TO MODIFY THE INITIALIZATION OF THE GAME VARIABLES.


# game loop
while True:
    # x: x position of your pod
    # y: y position of your pod
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    x, y, next_checkpoint_x, next_checkpoint_y = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # Edit this line to output the target position
    # and thrust (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " 50")

# 2st LEVEL

import sys
import math

# This code automatically collects game data in an infinite loop.
# It uses the standard input to place data into the game variables such as x and y.
# YOU DO NOT NEED TO MODIFY THE INITIALIZATION OF THE GAME VARIABLES.


# game loop
while True:
    # x: x position of your pod
    # y: y position of your pod
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    x, y, next_checkpoint_x, next_checkpoint_y = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # Edit this line to output the target position
    # and thrust (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " 99")


#stX3 LEVEL
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
target_checkpoints = []
if_BOOST = True
pod_force_field_size = 400
max_wide = 16000
max_high = 9000
checkpoint_radius = 600
max_diagonal = math.sqrt(max_wide^2 + max_high^2)
# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    

    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    thrust = 100
    if next_checkpoint_angle > 90 or next_checkpoint_angle < -90:
        thrust = 0
    else:
        thrust = 100
    
    if(next_checkpoint_dist > (4 * checkpoint_radius) and if_BOOST == True and thrust > 50):
        print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " BOOST")
        if_BOOST = False
        print("BOOST", file=sys.stderr, flush=True)
    else:
        print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " "+ str(thrust))
#st4 LEVEL

    
    
