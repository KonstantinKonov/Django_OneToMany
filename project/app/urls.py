from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_company/', views.create_company, name='create company'),
    path('create_product/', views.create_product, name='create product'),
]
