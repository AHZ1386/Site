from django.urls import path
from . import views
app_name = 'Custom_admin'

urlpatterns = [
    path('',views.index,name='index'),
    path('products/',views.ProductListView.as_view(),name='products'),
    path('users/',views.UserListView.as_view(),name='users'),
    path('orders/',views.OrderListView.as_view(),name='orders'),
    path('create-product/',views.ProductCreateView.as_view(),name='create_product'),
    path('update-product/<int:pk>', views.ProductUpdateView.as_view(), name='update_product'),
    path('delete-product/<int:pk>', views.ProductDeleteView.as_view(), name='delete_product'),
    path('order-update/<int:pk>', views.OrderUpdateView.as_view(), name='order_update'),
    path('category-create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('brand-create/', views.BrandCreateView.as_view(), name='brand_create'),
    path('brands/',views.BrandListView.as_view(), name='brands'),
    path('categories/',views.CategoryListView.as_view(), name='categorys'),
    # path('order-detail/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('order-detail/<int:pk>/', views.order_detail, name='order_detail'),
    path('print/<int:pk>',views.print_order_invoice,name='print'),
]