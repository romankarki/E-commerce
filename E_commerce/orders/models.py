from django.db import models

from products.models import Product

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Order(models.Model):

    user = models.ForeignKey(User,related_name='orders',on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='orders',on_delete=models.CASCADE)
    ordered_date= models.DateField(auto_now=True, blank=True)
    no_of_orders = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return self.user.username+"--->"+self.product.name
    

