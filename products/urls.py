from django.urls import path
from . import views
from .models import Product


urlpatterns=[path("",views.index),
             path("news",views.new),
             path("<product_id>",views.detail)

             ]
