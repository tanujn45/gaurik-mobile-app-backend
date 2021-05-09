from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"
        db_table = "Categories"
    
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Products"
        db_table = "Products"
    
    def __str__(self):
        return self.title