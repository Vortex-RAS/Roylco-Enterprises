from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from app1.forms import CustomerEditForm, CustomerForm, OrderForm, OrderProductForm, ProductForm
from app1.models import Customer, Order, OrderProduct, Product
from django.db.models import Q
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.
def home(request):
    return render(request,"home.html")

def order_entry(request):
    OrderProductFormSet = modelformset_factory(OrderProduct, form=OrderProductForm, extra=1)

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        product_formset = OrderProductFormSet(request.POST, queryset=OrderProduct.objects.none())

        if order_form.is_valid() and product_formset.is_valid():
            order = order_form.save()
            for product_form in product_formset:
                product = product_form.save(commit=False)
                product.order = order
                product.save()

            return redirect('order_preview', pk=order.pk)
    else:
        order_form = OrderForm()
        product_formset = OrderProductFormSet(queryset=OrderProduct.objects.none())

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
