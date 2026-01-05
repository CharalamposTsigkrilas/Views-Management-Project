from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required
def page3(request):
    return render(request, 'app3/page3.html')