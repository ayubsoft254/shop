from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from sales.models import Product, Customer, Order, OrderDetail


# Create your views here.
@login_required
def site_home(request):    
    return render(request, 'index.html')

@login_required
def products_list(request):
    products = Product.objects.all()
    context = {'products':products}    
    return render(request, 'products.html', context)

@login_required
def customers(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'customers.html', context)

@login_required
def orders(request, customer_id):

    current_customer = Customer.objects.get(id=customer_id)

    if current_customer:
        orders = Order.objects.filter(customer=current_customer)
        context = {'orders': orders}
        
    context.update({'customer': current_customer})
    return render(request, 'orders.html', context)

@login_required
def order_details(request, order_id):
    selected_order = Order.objects.get(id=order_id)
    order_details = OrderDetail.objects.filter(order=selected_order)
    
    for detail in order_details:
        detail.amount = detail.quantity * detail.product.price
        
    context = {
        'order': selected_order,
        'order_details': order_details
    }
    return render(request, 'order_details.html', context)