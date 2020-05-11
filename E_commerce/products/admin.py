from django.contrib import admin

# Register your models here.
from products.models import Product

class ProductAdmin(admin.ModelAdmin):

    search_fields=['name','brand','description']
    list_display=['name','brand','price','in_stock']
    

admin.site.register(Product,ProductAdmin)
