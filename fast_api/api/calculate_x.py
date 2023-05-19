import math

def calculate_x(a,b,c):
    b_square = b**2
    four_a_c = 4*a*c
    if (b_square - four_a_c) < 0:
        raise ValueError("Invalid Inputs")
    square_root = math.sqrt(b_square - four_a_c)
    x1 = (-b + square_root)/(2*a)
    x2 = (-b - square_root)/(2*a)
    return x1, x2