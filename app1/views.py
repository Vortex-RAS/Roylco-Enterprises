from django.shortcuts import get_object_or_404, redirect, render
from app1.forms import CustomerEditForm, CustomerForm, ProductForm
from app1.models import Customer, Product
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,"home.html")

def order_entry(request):
    return render(request,"order_entry.html")



def customer_detail(request, id):
    customer = get_object_or_404(Customer, pk=id)
    return render(request, 'customer_detail.html', {'customer': customer})

def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    
    if request.method == 'POST':
        form = CustomerEditForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_detail', id=customer.pk)  # Ensure this matches your URL pattern name
    else:
        form = CustomerEditForm(instance=customer)
    
    return render(request, 'customer_edit.html', {'form': form, 'customer': customer})

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_index')  # Redirect to the customer index or another page after deletion
    #SSSreturn render(request, 'customer_confirm_delete.html', {'customer': customer})
def customer_index(request):
    search_query = request.GET.get('search', '')  # Get search term from query parameters

    if search_query:
        customers = Customer.objects.filter(
            Q(name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(customer_id__icontains=search_query)
        )
    else:
        customers = Customer.objects.all()

    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_index')

    context = {
        'customers': customers,
        'form': form,
        'search_query': search_query,
    }
    return render(request, 'customer_index.html', context)
def add_customer(request):
    return render(request,"add_customer.html")

def product_index(request):
    products = Product.objects.all()
    return render(request, 'product_index.html', {'products': products})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_index')
    else:
        form = ProductForm()
    return render(request, 'product_index.html', {'form': form})

