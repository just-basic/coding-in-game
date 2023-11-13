import sys
import math

class Ship:
    def __init__(self, x, y, h_speed, v_speed, fuel, rotate, power):
        self.x = x 
        self.y = y 
        self.h_speed = h_speed 
        self.v_speed = v_speed 
        self.fuel = fuel 
        self.rotate = rotate 
        self.power = power
class Coordinates:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
class Surface:
    def __init__(self,number_of_vertices):
        self.number_of_vertices = number_of_vertices
        self.vertices = []
        self.landing_area = []
    def add_vertecies(self, x: int, y: int):
        self.vertices.append([x, y])
    def flat(self):
        for index, vertex in enumerate(self.vertices):
            # while index < len(self.vertices) or self.landing_area != []:
            if vertex[1] == self.vertices[index + 1][1]:
                self.landing_area.append(vertex)
                self.landing_area.append(self.vertices[index + 1])
                info("Flat at: "+ str(self.landing_area[0]) + str(self.landing_area[1]))
                break
            else:
                pass
def info(message: str):
    print(message, file=sys.stderr, flush=True)
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
surface: Surface = Surface(surface_n)
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    surface.add_vertecies(land_x, land_y)
surface.flat()


# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    if(y < (surface.landing_area[0][1] + 700) or v_speed < -20):
        info("Landing" + str(v_speed))
        print("0 4")
    else:
        print("0 3")
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    
    # 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).

