from django.urls import path

from . import views
app_name = 'Account'

urlpatterns = [

    path('profile', views.profile, name='profile'),
    path('login', views.LoginClassView.as_view(), name='login'),
    path('edit-profile', views.UserProfileUpdateView.as_view(), name='edit_profile'),
    path('singin', views.signup, name='singin'),
    path('registration',views.register,name='registration'),
    path('shopping-cart', views.user_cart, name='shopping_cart'),
    path('orders', views.user_orders, name='orders'),
    path('change-password', views.change_password, name='change_password'),
    path('logout',views.logo_out,name='logout'),
    path('edit-address/<int:address_id>',views.edit_address , name="edit_address"),
    path('add-address',views.add_user_address,name='add_address'),
    path('select-address/<int:address_id>',views.select_user_address,name='select_user_address'),
]
