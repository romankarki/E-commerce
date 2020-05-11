from django.contrib import admin

# Register your models here.
from orders.models import Order

class OrderAdmin(admin.ModelAdmin):

    search_fields=['ordered_date']
    list_display=['product','user','ordered_date']
    list_filter = ['ordered_date']


admin.site.register(Order,OrderAdmin)
