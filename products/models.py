from django.db import models

# Create your models here.

class Product(models.Model):
    prd_no = models.TextField(max_length=30)
    prd_nm = models.TextField(max_length=100)
    prd_img = models.ImageField(upload_to='uploads/%Y/%m/%d/product')
    content = models.TextField(max_length=500, null=True, blank=True)
    create_dt = models.DateTimeField(auto_now_add=True)
