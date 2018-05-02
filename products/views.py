from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView, DetailView
from products.models import Product

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class ProductLV(ListView):
    model = Product
    template_name = 'product_list.html'

#class ProductDV(DetailView):
#    model = Product
#    template_name = 'product_Detail.html'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['prd_no','prd_nm','content','prd_img']
    success_url = reverse_lazy('products:index')
    def form_valid(self, form):
        return super(ProductCreateView, self).form_valid(form)

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['prd_nm','content','prd_img']
    success_url = reverse_lazy('products:index')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('products:index')
