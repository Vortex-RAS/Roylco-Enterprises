from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("order_entry", views.order_entry, name="order_entry"),
    path("order_preview/<int:pk>/", views.order_preview, name="order_preview"),
    path("customer_index", views.customer_index, name="customer_index"),    
    path("order_index", views.order_index, name="order_index"),    
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),    
    path('product-edit/<int:pk>/edit/', views.product_edit, name='product_edit'),    
    path('customer/<int:id>/', views.customer_detail, name='customer_detail'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'), 
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'), 
    path("add_customer", views.add_customer, name="add_customer"),
    path("product_index", views.product_index, name="product_index"),
    path("add_product", views.add_product, name="add_product"),
    path('order_preview_pdf/<int:pk>/', views.order_preview_pdf, name='order_preview_pdf'),



]