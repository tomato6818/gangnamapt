from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('prd_no', 'prd_nm', 'prd_img', 'content')

admin.site.register(Product, ProductAdmin)
