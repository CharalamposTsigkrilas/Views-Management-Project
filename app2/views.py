from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required
def page2(request):
    return render(request, 'app2/page2.html')