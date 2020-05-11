from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'cart'

urlpatterns = [
     url(r'^cart/(?P<pk>\d+)/$',views.CartListView.as_view(),name="cart_list"),
     url(r'^cart/delete/(?P<pk>\d+)/$',views.CartDeleteView.as_view(),name="cart_delete"),
     url(r'^cart/create/(?P<pk>\d+)/$',views.CartCreateView.as_view(),name="create"),
]
