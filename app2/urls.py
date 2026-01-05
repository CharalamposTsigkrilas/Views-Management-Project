from django.urls import path
from .views import page2

urlpatterns = [
    path('', page2, name='page2'),
]