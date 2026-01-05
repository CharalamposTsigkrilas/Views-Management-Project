from django.shortcuts import render

# Create your views here.

def page2(request):
    return render(request, 'app2/page2.html')