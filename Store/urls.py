from django.urls import path

from . import views
app_name = 'store'

urlpatterns = [
    path('', views.AllProductsView.as_view(), name='all-product'),

    path('category-detail/<str:slug>/', views.CategoryDetailViwe.as_view(), name='category_detail'),
    path('product-detail/<str:slug>/', views.product_detail, name='product_detail'),


    
]
