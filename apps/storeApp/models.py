from __future__ import unicode_literals
from django.db import models
import re
from djmoney.models.fields import MoneyField

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

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors['f_name_short'] = "First Name must be at least 2 characters."
        if len(postData['first_name']) > 255:
            errors['f_name_long'] = "First Name can't be more than 50 characters."
        if not NAME_REGEX.match(postData['first_name']):
            errors['f_name_regex'] = "First Name can only contain letters; no numbers, spaces or special characters."

        if len(postData['last_name']) < 2:
            errors['l_name_short'] = "Last Name must be at least 2 characters."
        if len(postData['last_name']) > 255:
            errors['l_name_long'] = "Last Name can't be more than 50 characters."
        if not NAME_REGEX.match(postData['last_name']):
            errors['l_name_regex'] = "Last Name can only contain letters; no numbers, spaces or special characters."

        if len(postData['email']) == 0:
            errors['req_email'] = "Email Required."
        if len(postData['email']) > 255:
            errors['long_email'] = "Email is too long.  Must be no more than 50 characters."
        if not EMAIL_REGEX.match(postData['email']):
            errors['email_regex'] = "Not a valid email address."
        existing_email = User.objects.filter(email=postData['email'])
        if len(existing_email) > 0:
            errors['email_exists'] = "Email Address is already registered to another user."

        if len(postData['password']) < 8:
            errors['email_short'] = "Password must be at least 8 characters."
        if len(postData['password']) > 200:
            errors['email_long'] = "Password is too long.  Must be no more than 50 characters."
        if postData['password'] != postData['password_conf']:
            errors['no_pw_match'] = "Password confirmation failed.  Does not match."
        return errors 
        
        # -----    Models    -----

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    wants_newsletter = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    # orders = List of orders associated with this User.
    # articles = List of Articles associated with this User.

class Category(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CategoryManager()
    # brands = List of Brands associated with this Category.
    # products = List of Products associated with this Category.

class Brand(models.Model):
    name = models.CharField(max_length=128)
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
    inventory = models.IntegerField()
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
