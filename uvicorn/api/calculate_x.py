import math
import json

def calculate_x(a,b,c):
    if a == 0:
        return {"error":"The value of a not equal to zero"}
    b_square = b**2
    four_a_c = 4*a*c
    if (b_square - four_a_c) < 0:
        return {"error":"Invalid Inputs"}
    square_root = math.sqrt(b_square - four_a_c)
    x1 = (-b + square_root)/(2*a)
    x2 = (-b - square_root)/(2*a)
    return {"x1":x1,"x2":x2}