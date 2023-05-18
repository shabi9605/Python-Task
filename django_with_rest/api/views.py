
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from . serializers import QuadraticSerializer

import math


# Create your views here.

def calculate_x(a,b,c):
    b_square = b**2
    four_a_c = 4*a*c
    if (b_square - four_a_c) < 0:
        raise ValueError("Invalid Inputs")
    square_root = math.sqrt(b_square - four_a_c)
    x1 = (-b + square_root)/(2*a)
    x2 = (-b - square_root)/(2*a)
    return x1, x2

class QuadraticViewSet(GenericAPIView):
    def post(self, request):
        serializer = QuadraticSerializer(data = request.data)
        if serializer.is_valid():
            a = request.data.get("a")
            b = request.data.get("b")
            c = request.data.get("c")
            try:
                x1, x2 = calculate_x(a,b,c)
                return Response({"x1":x1,"x2":x2})
            except ValueError:
                return Response({"error":"Invalid Input"})
        else:
            return Response(serializer.errors)


