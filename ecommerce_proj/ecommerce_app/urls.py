from django.urls import path
from . import views

urlpatterns = [
    # Pages
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('kitchen', views.kitchen, name='kitchen'),
    path('bed_bath', views.bed_bath, name='bed_bath'),
    path('cart', views.cart, name='cart'),

    # Helper functions
    path('search', views.search, name='search'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('cart_counter', views.cart_counter, name='cart_counter'),
]