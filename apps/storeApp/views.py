from django.shortcuts import render, redirect
from .models import Category, Brand, Product, Order, Article, User
from django.contrib import messages

# Create your views here.
def index (request):
    # context = [
    #     "stuff":stuff,
    # ]
    return render(request,'index.html')

def home(request):
    return render(request, "home.html")

def directions(request):
    return render(request, "directions.html")

def cart(request):
    return render(request, "cart.html")

def login(request):
    return render(request, "login.html")

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
        errors = Product.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/add_product')
        else:
            category_to_add = Category.objects.get(id=request.POST['product_category'])
            brand_to_add = Brand.objects.get(id=request.POST['product_brand'])
            image_to_add = request.FILES['product_image']
            Product.objects.create(name=request.POST['product_name'], description=request.POST['product_description'], image=image_to_add, price=request.POST['product_price'], category=category_to_add, brand=brand_to_add)
            brand_to_add.categories.add(category_to_add)
        return redirect('/add_product')

# path('products/<int:product_id>', views.product_detail),
def product_detail(request, product_id):
    this_product = Product.objects.filter(id=product_id)
    if len(this_product) > 0:
        this_product = this_product[0]
        context = {
            'this_product': this_product,
        }
        return render(request, "product_detail.html", context)
    return redirect('/')


def create_category(request):
    if request.method == "POST":
        errors = Category.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/add_product')
        else:
            Category.objects.create(name=request.POST['new_category'])
            return redirect('/add_product')
    return redirect('/add_product')

def create_brand(request):
    if request.method == "POST":
        errors = Brand.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/add_product')
        else:
            category_to_add = Category.objects.get(id=request.POST['brand_category'])
            new_brand = Brand.objects.create(name=request.POST['new_brand'])
            new_brand.categories.add(category_to_add)
            return redirect('/add_product')
    return redirect('/add_product')