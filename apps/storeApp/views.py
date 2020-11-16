from django.shortcuts import render, redirect
from .models import Category, Brand, Product

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

def add_product(request):
    context = {
        'all_categories': Category.objects.all(),
        'all_brands': Brand.objects.all(),
        'last_product': Product.objects.last(),
    }
    return render(request, 'add_product.html', context)

def create_product(request):
    if request.method == "POST":
        category_to_add = Category.objects.get(id=request.POST['product_category'])
        brand_to_add = Brand.objects.get(id=request.POST['product_brand'])
        Product.objects.create(name=request.POST['product_name'], description=request.POST['product_description'], image=request.POST['product_image'], price=request.POST['product_price'], category=category_to_add, brand=brand_to_add)
        return redirect('/add_product')