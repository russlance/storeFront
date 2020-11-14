from django.shortcuts import render, redirect

# Create your views here.
def index (request):
    # context = [
    #     "stuff":stuff,
    # ]
    return render(request,'index.html')

def news(request):
    # Maybe there's some logic here that returns the queryset of the most recent news items.
    # ajax on the page would replace the most recent articles with some page navigation?
    return render(request, 'news.html')

def events(request):
    return render(request, 'events.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')