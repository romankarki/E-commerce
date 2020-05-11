from django.db import models

# Create your models here.
from products.models import Product

from django.contrib.auth import get_user_model
User = get_user_model()

class Cart(models.Model):

    user = models.ForeignKey(User,related_name="carts",on_delete=models.CASCADE)
    product =  models.ForeignKey(Product,related_name = 'carts',blank = True, null =True, on_delete = models.CASCADE)
    added_date = models.DateField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.user.username+"---->"+self.product.name
    


