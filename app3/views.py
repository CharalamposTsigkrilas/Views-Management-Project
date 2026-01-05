from django.shortcuts import render

# Create your views here.

def page3(request):
    return render(request, 'app3/page3.html')