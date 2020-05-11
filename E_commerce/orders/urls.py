from django.urls import path
from django.conf.urls import url
from orders import views
app_name="orders"

urlpatterns = [
    path("",views.OrderTemplate.as_view(),name="Landing"),
    url(r'^(?P<pk>\d+)/$',views.OrderListView.as_view(),name="orders_list"),
    url(r'^create/(?P<pk>\d+)/$',views.OrderCreateView.as_view(),name="order_create")

]

