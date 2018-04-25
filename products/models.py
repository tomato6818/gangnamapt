from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    prd_no = models.TextField(max_length=30)
    prd_nm = models.TextField(max_length=100)
    prd_img = models.ImageField(upload_to='uploads/%Y/%m/%d/product', null=True)
    content = models.TextField(max_length=500, null=True, blank=True)
    create_dt = models.DateTimeField(auto_now_add=True)
    #owner = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.prd_nm
