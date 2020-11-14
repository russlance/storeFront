from django.shortcuts import render, redirect

# Create your views here.
def index (request):
    context = [
        "stuff":stuff,
    ]
    return render (request,'money_app/home.html', context)