from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length= 128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # brands = List of Brands associated with this Category.
    # products = List of Products associated with this Category.

class Brand(models.Model):
    name = models.CharField(max_length= 128)
    categories = models.ManyToManyField(Category, related_name="brands")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # products = List of Products associated with this Brand

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to='media')
                # access image details: productObject.image.name  /  productObject.image.path
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name="products", on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # orders = List of Orders containing this product.

class Order(models.Model):
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    total = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    products_ordered = models.ManyToManyField(Product, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Article(models.Model):
    author = models.ForeignKey(User, related_name="articles", on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    content  = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
