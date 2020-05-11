from django.contrib import admin
from .models import Cart
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    #fields = ['product','user']
    search_fields=['added_date']
    list_filter=['user','added_date']
    list_display=['user','product','added_date']

    
admin.site.register(Cart,CartAdmin)

