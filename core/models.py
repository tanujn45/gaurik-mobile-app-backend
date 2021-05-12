from django.db import models
import uuid

class User(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, null=False)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, null=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'User'

    def __str__(self):
        return str(self.name)

class Category(models.Model):
    key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "Categories"
        db_table = "Categories"
    
    def __str__(self):
        return self.title

class Product(models.Model):
    key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True) 
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = "Products"
        db_table = "Products"
    
    def __str__(self):
        return self.title

class Order(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Orders'

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'OrderItem'

    def __str__(self):
        return str(self.order.uid)
