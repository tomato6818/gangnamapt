# Generated by Django 2.0.3 on 2018-04-03 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20180402_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prd_img',
            field=models.ImageField(upload_to='uploads/%Y/%m/%d/product'),
        ),
    ]