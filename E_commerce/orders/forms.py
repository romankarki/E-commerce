# from django import forms

# def is_instock(stock,order):
#     if stock > order or stock == order:
#         return order
#     else:
#         return 0


# class OrderForm(forms.Form):

#     no_of_orders = forms.PositiveIntegerField(
#         label = 'in_stock',
#         widget = forms.NumberInput(attrs={'class':'input'})
#     )

#     def clean_no_of_orders(self):

#         data  = self.cleaned_data.get('no_of_orders')

#         if not is_in

#         return data
