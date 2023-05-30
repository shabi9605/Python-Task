import sys
from django.conf import settings
from django.urls import path
from django.http import HttpResponse
import math
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django import forms
from django.core import validators


# settings configuration
settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisthesecretkey',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=('django.middleware.common.CommonMiddleware',
                        'django.middleware.csrf.CsrfViewMiddleware',
                        'django.middleware.clickjacking.XFrameOptionsMiddleware')
)

# function for calculating x
def calculate_x(a,b,c):
    b_square = b**2
    four_a_c = 4*a*c
    if (b_square - four_a_c) < 0:
        raise ValueError("Invalid Inputs")
    square_root = math.sqrt(b_square - four_a_c)
    x1 = (-b + square_root)/(2*a)
    x2 = (-b - square_root)/(2*a)
    return x1, x2



# forms.py section
def validate_a(a):
    if a == 0:
        print("hi")
        raise forms.ValidationError("The value of a not equal to zero") 
    
    

class QuadraticForm(forms.Form):
    a = forms.FloatField(required=True,validators=[validate_a])
    b = forms.FloatField(required=True,)
    c = forms.FloatField(required=True,)

# end forms section

# write our functions here
def index(request): 
    return HttpResponse('Hello World shbai')


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


# urls
urlpatterns = [
    path('test/', index),
    path('api/', quadratic_eqn)
]
    

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)