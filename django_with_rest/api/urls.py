from django.urls import path
from . views import QuadraticViewSet


urlpatterns = [
    path('',QuadraticViewSet.as_view(),name='quadratic_viewSet')
]