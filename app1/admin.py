from django.contrib import admin
from .models import Customer,Product,CustomerProduct,Order,WorkOrder

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(CustomerProduct)
admin.site.register(Order)
admin.site.register(WorkOrder)
