from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required
def page1(request):
    return render(request, 'app1/page1.html')