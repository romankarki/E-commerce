from django.shortcuts import render
from django.urls import reverse
# Create your views here.
from django.views.generic import ListView,TemplateView,DetailView,DeleteView,CreateView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from orders.models import Order
from products.models import Product


class OrderTemplate(TemplateView):
    template_name = "orders/orders_home.html"


class OrderListView(LoginRequiredMixin,ListView):
    model = Order
    template_name = "orders/orders_list.html"
    context_object_name = "orders"


       

    def get_queryset(self):

        queryset =  super().get_queryset()
        r = queryset.filter(user = self.kwargs.get('pk'))
        query = self.request.GET.get('search')
        if query:
            result = r.filter(product__name__contains=query)
        else:
           result = r.all()
        return result
        



class OrderCreateView(LoginRequiredMixin,CreateView):
    model = Order
    template_name = "orders/order_form.html"
    fields = ('product','user','no_of_orders')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        p = Product.objects.get(pk=self.kwargs['pk'])
        prod = p.name
        stock = p.in_stock
        context["in_stock"] = stock
        context["prod"] = prod
        return context
    

    def get_success_url(self):
        p = Product.objects.get(pk=self.kwargs['pk'])
        p.in_stock = p.in_stock -self.object.no_of_orders
        p.save()
        return reverse('orders:orders_list', kwargs={'pk': self.object.user.id})
       #return reverse('orders:Landing')

    def form_valid(self, form):
        form.instance.user = self.request.user
        if form.instance.no_of_orders <= form.instance.product.in_stock:
            return super(OrderCreateView, self).form_valid(form)
        else:
            p = Product.objects.get(pk=self.kwargs['pk'])
            prod = p.name
            stock = p.in_stock
            return render(self.request, 'orders/orders_home.html',context={'in_stock':stock,'prod':prod})

    def get_initial(self):
        initial = super(OrderCreateView, self).get_initial()
        initial['product'] = Product.objects.get(pk=self.kwargs['pk'])
        initial['user'] = self.request.user
        return initial






    



