from django.db import models

class Category(models.Model):
    parent=models.ForeignKey('self',blank=True,null=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    avator=models.ImageField(blank=True,upload_to='Categories')
    is_enable=models.BooleanField(default=True)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='Categgories'
        verbose_name='Category'
        verbose_name_plural='Categories'
class Product(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    avator=models.ImageField(blank=True,upload_to='Categories')
    is_enable=models.BooleanField(default=True)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='Products'
        verbose_name='Product'
        verbose_name_plural='Products'
class File(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    avator=models.ImageField(blank=True,upload_to='Categories')
    is_enable=models.BooleanField(default=True)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='Files'
        verbose_name='File'
        verbose_name_plural='Files'