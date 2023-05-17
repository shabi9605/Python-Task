from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . forms import QuadraticForm
import math

# Create your views here.

@csrf_exempt
def quadratic_eqn(request):
    form = QuadraticForm()
    if request.method == 'POST':
        body = json.loads(request.body.decode("utf-8")) # this converting to python objects because its getting as a string
        form = QuadraticForm(body)
        if form.is_valid():
            try:
                x1,x2 = calculate_x(body["a"],body["b"],body["c"])
                return JsonResponse({"x1":x1,"x2":x2})
            except ValueError:
                return JsonResponse({"error":"Invalid Input"})
        else:
            return JsonResponse(form.errors,safe=False)
        

def calculate_x(a,b,c):
    b_square = b**2
    four_a_c = 4*a*c
    if (b_square - four_a_c) < 0:
        raise ValueError("Invalid Inputs")
    square_root = math.sqrt(b_square - four_a_c)
    x1 = (-b + square_root)/(2*a)
    x2 = (-b - square_root)/(2*a)
    return x1, x2


        
