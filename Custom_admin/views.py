from Store.models import Order, Product, Category, Brand
from django.shortcuts import render
from  Account.models import User
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import forms
from django.http import Http404
from django.contrib.auth.decorators import user_passes_test
from .decorator import superuser_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_superuser


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    context = {
        'orders': Order.objects.exclude(status='do').count(),
        'users': User.objects.all().count(),
        'products': Product.objects.count(),

    }
    return render(request, 'Custom_admin/index.html',context)
@method_decorator(user_passes_test(is_admin), name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    form_class = forms.ProductUpdateForm
    template_name = 'Custom_admin/Product/product_update.html'
    success_url = '/custom-admin/products/'
@method_decorator(user_passes_test(is_admin), name='dispatch')
class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 20
    template_name = 'Custom_admin/Product/product_list.html'
@method_decorator(user_passes_test(is_admin), name='dispatch')
class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    paginate_by = 10
    template_name = 'Custom_admin/Order/order_list.html'
# @method_decorator(user_passes_test(is_admin), name='dispatch')
# class OrderDetailView(DetailView):
#     model = Order
#     context_object_name = 'order'
#     template_name = 'Custom_admin/Order/order_detail.html'

def order_detail(request, pk):
    context = {
        'order': Order.objects.get(pk=pk)
    }
    print(Order.objects.get(pk=pk).products.count())
    return render(request, 'Custom_admin/Order/order_detail.html',context)
@method_decorator(user_passes_test(is_admin), name='dispatch')
class UserListView(ListView):
    model = User
    context_object_name = 'users'
    paginate_by = 30
    template_name = 'Custom_admin/User/user_list.html'


@method_decorator(user_passes_test(is_admin), name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    form_class = forms.ProductCreateForm
    template_name = 'Custom_admin/Product/product_create.html'
    success_url = '/custom-admin/products/'


@method_decorator(user_passes_test(is_admin), name='dispatch')
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'Custom_admin/Product/product_delete.html'
    success_url = '/custom-admin/products/'
@method_decorator(user_passes_test(is_admin), name='dispatch')
class OrderUpdateView(UpdateView):
    model = Order
    form_class = forms.OrderUpdateForm
    template_name = 'Custom_admin/Order/order_update.html'
    success_url = '/custom-admin/orders/'
@method_decorator(user_passes_test(is_admin), name='dispatch')
class BrandCreateView(CreateView):
    model = Brand
    form_class = forms.BrandCreateForm
    template_name = 'Custom_admin/Product/brand_create.html'
    success_url = '/custom-admin/'
@method_decorator(user_passes_test(is_admin), name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    form_class = forms.CategoryCreateForm
    template_name = 'Custom_admin/Product/category_create.html'
    success_url = '/custom-admin/categories/'
@method_decorator(user_passes_test(is_admin), name='dispatch')
class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'Custom_admin/Product/category_list.html'
@method_decorator(user_passes_test(is_admin), name='dispatch')
class BrandListView(ListView):
    model = Brand
    context_object_name = 'brands'
    template_name = 'Custom_admin/Product/brand_list.html'