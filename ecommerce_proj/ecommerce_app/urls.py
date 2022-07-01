from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/home', views.home, name='home'),
    path('/kitchen', views.kitchen, name='kitchen'),
    path('/bed_bath', views.bed_bath, name='bed_bath'),
    path('search', views.search, name='search'),
]