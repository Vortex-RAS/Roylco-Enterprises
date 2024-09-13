from django.db import models

# Customer Model
class Customer(models.Model):
    name = models.CharField(max_length=255)
    customer_id = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    fax = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name


# Product Model
class Product(models.Model):
    part_code = models.CharField(max_length=100, unique=True)
    part_name = models.CharField(max_length=255)
    details = models.TextField(blank=True, null=True)
    material_used = models.CharField(max_length=255)

    def __str__(self):
        return self.part_name

# CustomerProduct Model for adding products to a customer's list
class CustomerProduct(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} - {self.product.part_name}"

# Order Model
# Order Model
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    po_number = models.CharField(max_length=100, unique=True)
    part_code = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    due_date = models.DateField()
    ship_to_address = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='ship_orders')
    status_choices = [
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    ]
    status = models.CharField(max_length=50, choices=status_choices, default='In Progress')

    def __str__(self):
        return f"PO Number: {self.po_number} - {self.status}"

# WorkOrder Model
class WorkOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='work_orders')
    employee_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Work Order for {self.order.po_number}"
