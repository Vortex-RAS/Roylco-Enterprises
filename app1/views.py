from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def order_entry(request):
    return render(request,"order_entry.html")

def customer_index(request):
    return render(request,"customer_index.html")

def add_customer(request):
    return render(request,"add_customer.html")
