from Store.models import Product
from django.shortcuts import render
from django.views.generic import ListView


class InedexListView(ListView):
    model = Product
    paginate_by = 1
    context_object_name = 'products'
    template_name = 'Pages/index.html'