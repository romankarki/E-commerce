from django.shortcuts import render
from django.views.generic  import ListView,DetailView,TemplateView
from products.models import Product
# Create your views here.


class IndexView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"

class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
       result = super(ProductListView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Product.objects.filter(name__contains=query)
          result = postresult
       else:
           result = Product.objects.all()
       return result


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = 'product_details'




