from django.urls import path
from .views import page3

urlpatterns = [
    path('', page3, name='page3'),
]