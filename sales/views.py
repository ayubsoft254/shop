from django.shortcuts import render
from sales.models import Product, Customer

# Create your views here.
def site_home(request):
    return render(request, 'index.html')

def products_list(request):
    products = Product.objects.all()
    context = {'products':products}    
    return render(request, 'products.html', context)

def customers(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'customers.html', context)