from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from app1.forms import CustomerEditForm, CustomerForm, OrderForm, OrderProductForm, ProductEditForm, ProductForm
from app1.models import Customer, Order, OrderProduct, Product
from django.db.models import Q
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    orders = Order.objects.all()
    return render(request,"home.html",{"orders":orders})
@csrf_exempt
def order_entry(request):
    OrderProductFormSet = modelformset_factory(OrderProduct, form=OrderProductForm, extra=1)

    # Debug: Check request method
    print(f"Request method: {request.method}")

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        product_formset = OrderProductFormSet(request.POST, queryset=OrderProduct.objects.none())

        # Debug: Print POST data and check form validity
        print(f"POST data: {request.POST}")
        print(f"Order form valid: {order_form.is_valid()}")
        print(f"Product formset valid: {product_formset.is_valid()}")

        if order_form.is_valid() and product_formset.is_valid():
            order = order_form.save()

            # Debug: Print saved order details
            print(f"Saved Order: {order}")

            for product_form in product_formset:
                product = product_form.save(commit=False)
                product.order = order
                product.save()

                # Debug: Print saved product details
                print(f"Saved Product: {product}")

            return redirect('order_preview', pk=order.pk)
        else:
            # Debug: Print form errors if validation fails
            print(f"Order form errors: {order_form.errors}")
            print(f"Product formset errors: {product_formset.errors}")
    else:
        order_form = OrderForm()
        product_formset = OrderProductFormSet(queryset=OrderProduct.objects.none())

    # Debug: Indicate rendering the order entry page
    print("Rendering order entry page")

    return render(request, 'order_entry.html', {
        'order_form': order_form,
        'product_formset': product_formset,
    })


def order_preview(request, pk):
    order = get_object_or_404(Order, pk=pk)
    products = order.order_products.all()  # Fetch related order products

    return render(request, 'order_preview.html', {
        'order': order,
        'products': products,
    })
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

def order_index(request):
    orders = Order.objects.all()

    # Create a list to store order products for each order
    orders_with_products = []
    for order in orders:
        order_products = order.order_products.all()  # Get related products
        orders_with_products.append({
            'order': order,
            'order_products': order_products
        })

    return render(request, 'order_index.html', {'orders_with_products': orders_with_products})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        form = ProductEditForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_index')  # Ensure this matches your URL pattern name
    else:
        form = ProductEditForm(instance=product)
    
    return render(request, 'product_edit.html', {'form': form, 'product': product})

def product_delete(request, pk):
    print(pk)
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_index') 
    
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_index')
    else:
        form = ProductForm()
    return render(request, 'product_index.html', {'form': form})



def order_preview_pdf(request, pk):
    # Fetch the order data (e.g., from the database)
    order = Order.objects.get(pk=pk)
    products = order.order_products.all()  # Fetch related order products

    print(order)

    # Use the template to render HTML content
    template_path = 'order_preview_pdf.html'  # The template for PDF rendering
    context = {'order': order,'products':products}
    template = get_template(template_path)
    html = template.render(context)

    # Create a PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Order_{order.po_number}.pdf"'

    # Convert the HTML to PDF
    pisa_status = pisa.CreatePDF(html, dest=response)

    # If there's an error in conversion, return an error response
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
    return response
