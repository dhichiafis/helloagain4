from django.shortcuts import render
def greet(request):
    return render(request,'hello/greeting.html')
# Create your views here.
