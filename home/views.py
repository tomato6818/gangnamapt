from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.db.models import Q
from django.shortcuts import render

from products.models import Product
from home.forms import PostSearchForm

class Home(FormView):
    form_class = PostSearchForm
    template_name = "home.html"

    def form_valid(self, form):
        schWord = '%s' % self.request.POST['search_word']
        product_list = Product.objects.filter(Q(prd_nm__icontains=schWord) | Q(content__icontains=schWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = product_list

        return render(self.request, self.template_name, context)
