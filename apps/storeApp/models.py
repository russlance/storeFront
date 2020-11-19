from __future__ import unicode_literals
from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User

        # -----    Validators    -----

class CategoryManager(models.Manager):
    def create_validator(self, postData):
        errors = {}
        if len(postData['new_category']) < 1:
            errors['no_name'] = "Add Category: Category Name Required."
        if Category.objects.filter(name=postData['new_category']):
            errors['duplicate_category'] = "Add Category: Category already exists."
        return errors

class BrandManager(models.Manager):
    def create_validator(self, postData):
        errors = {}
        if len(postData['new_brand']) < 1:
            errors['no_name'] = "Add Brand: Brand Name Required."
        if Brand.objects.filter(name=postData['new_brand']):
            errors['duplicate_category'] = "Add Brand: Brand already exists."
        if postData['brand_category'] == "":
            errors['no_category'] = "Add Brand:  Please choose a Category."
        return errors

class ProductManager(models.Manager):
    def create_validator(self, postData):
        errors = {}
        if len(postData['product_name']) < 1:
            errors['no_name'] = "Add Product: Product Name Required."
        if Product.objects.filter(name=postData['product_name']):
            errors['duplicate_product'] = "Add Product: Product already exists."
        if len(postData['product_description']) < 10 and len(postData['description']) > 0:
            errors['description'] = "Add Product: If a Description is entered, it must be at least 10 characters."
        if len(postData['product_price']) == 0:
            errors['no_price'] = "Add Product: Please enter a Price."
        if postData['product_category'] == "":
            errors['no_category'] = "Add Product: Please choose a Category."
        this_category = Category.objects.filter(id=postData['product_category'])
        if len(this_category) == 0:
            errors['category_not_exist'] = "Add Product: Category does not exist."
        if postData['product_brand'] == "":
            errors['no_brand'] = "Add Product: Please choose a Brand."
        this_brand = Brand.objects.filter(id=postData['product_brand'])
        if len(this_brand) == 0:
            errors['brand_not_exist'] = "Add Product: Brand does not exist."
        return errors
        

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length= 128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CategoryManager()
    # brands = List of Brands associated with this Category.
    # products = List of Products associated with this Category.

class Brand(models.Model):
    name = models.CharField(max_length= 128)
    categories = models.ManyToManyField(Category, related_name="brands")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BrandManager()
    # products = List of Products associated with this Brand

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to='media')
                # access image details: productObject.image.name  /  productObject.image.url
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name="products", on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManager()
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
