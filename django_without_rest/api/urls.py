
from django.urls import path
from . import views

urlpatterns = [
    path('',views.quadratic_eqn, name='quadratic_eqn'),
    
]