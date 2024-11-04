from django.views.generic import DetailView, ListView
from .forms import PostCommentForm
from .models import Product, Category, Comment
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404



def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    comments = product.product_comment.filter(confirmed=True)
    if request.user.is_authenticated == True :
        if request.method == 'POST':
            form = PostCommentForm(request.POST)
            if form.is_valid():
                text = form.cleaned_data['text']
                comment = Comment.objects.create(product=product,author=request.user,text=text,)
                comment.save()
                last_page = request.META.get('HTTP_REFERER')
                return HttpResponseRedirect(last_page)
        else:
            form = PostCommentForm()
            

        return render(request, 'Product/product_detail.html', {
        'product': product,
        'comments': comments,
        'form': form,
    })
    else:
        return render(request, 'Product/product_detail.html', {
        'product': product,
        'comments': comments,
    })


class CategoryDetailViwe(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'Product/category_detail.html'


class CategoryListView(ListView):
    model = Category
    paginate_by = 10
    template_name = 'Product/category_list.html'
    context_object_name = 'category'

class AllProductsView(ListView):
    model = Product
    paginate_by = 10
    template_name = 'Product/all_product.html'
    context_object_name = 'Product'