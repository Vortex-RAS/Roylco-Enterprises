from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("order_entry", views.order_entry, name="order_entry"),
    path("customer_index", views.customer_index, name="customer_index"),
    path("add_customer", views.add_customer, name="add_customer"),
    path("product_index", views.product_index, name="product_index"),
    path("add_product", views.add_product, name="add_product"),


]