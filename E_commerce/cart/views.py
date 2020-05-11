from django.shortcuts import render
from  cart.models import Cart
from django.urls import reverse_lazy,reverse
from  products.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.views.generic import ListView,TemplateView,DeleteView,DetailView,CreateView

from django.contrib.auth import get_user_model
User = get_user_model()


class CartListView(LoginRequiredMixin, ListView):
    model = Cart
    template_name = "cart_list.html"
    context_object_name = "carts"

    def get_queryset(self):
        queryset =  super().get_queryset()
        r =  queryset.filter(user = self.kwargs.get('pk'))
        query = self.request.GET.get('search')
        if query:
            result = r.filter(product__name__contains=query)
        else:
           result = r.all()
        return result


class CartDeleteView(LoginRequiredMixin,DeleteView):
    model = Cart

    def get_success_url(self):
        return reverse_lazy('cart:cart_list', kwargs={'pk': self.object.user.id})


class CartCreateView(LoginRequiredMixin,CreateView):
    model = Cart
    fields = ('product','user')    
    template_name = "cart/cart_form.html"
    context_object_name = 'cart'



    def get_success_url(self):
        return reverse('product:product_detail', kwargs={'pk': self.object.product.id})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CartCreateView, self).form_valid(form)

    def get_initial(self):
        initial = super(CartCreateView, self).get_initial()
        initial['product'] = Product.objects.get(pk=self.kwargs['pk'])
        initial['user'] = self.request.user
        return initial
    


  

    

