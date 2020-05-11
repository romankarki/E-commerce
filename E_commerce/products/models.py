from django.db import models

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='product_pics')
    category = models.CharField(max_length=200)
    brand  = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.TextField()
    in_stock = models.PositiveIntegerField()
    

    def __str__(self):
        return self.name
    
