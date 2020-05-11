from django.urls import path
from django.conf.urls import url 
from products.views import ProductListView,ProductDetailView

app_name = 'product'

urlpatterns = [
    path('',ProductListView.as_view(),name="product_list"),
    url(r'^(?P<pk>\d+)/$',ProductDetailView.as_view(),name="product_detail"),
]
