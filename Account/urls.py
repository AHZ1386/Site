from django.urls import path

from .views import user_cart, profile, LoginClassView, UserProfileUpdateView,signup,register,user_orders,change_password,logo_out,edit_address,add_user_address

app_name = 'Account'

urlpatterns = [

    path('profile/', profile, name='profile'),
    path('login/', LoginClassView.as_view(), name='login'),
    path('edit-profile/', UserProfileUpdateView.as_view(), name='edit_profile'),
    path('singin/',signup,name='singin'),
    path('registration/',register,name='registration'),
    path('shopping-cart/', user_cart, name='shopping_cart'),
    path('orders/', user_orders, name='orders'),
    path('change-password/', change_password, name='change_password'),
    path('logout/',logo_out,name='logout'),
    path('edit-address/<int:address_id>/',edit_address , name="edit_address"),
    path('add-address/',add_user_address,name='add_address'),
]
