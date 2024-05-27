from django.shortcuts import render

# Create your views here.
def site_home(request):
    return render(request, 'index.html')

def products_list(request):
    products =[
        {'name': 'hp',
         'price' : '20000',
         'stock' : 8},
        {'name': 'Lenovo',
         'price' : '30000',
         'stock' : 6},
        {'name': 'Dell',
         'price' : '15000',
         'stock' : 3},
        {'name': 'Toshiba',
         'price' : '200',
         'stock' : 9},
        {'name': 'Macbook',
         'price' : '25000',
         'stock' : 1},
        {'name': 'Samsung',
         'price' : '25000',
         'stock' : 6}

    ]
    context = {'products':products}    
    return render(request, 'products.html', context)

def customers(request):
    customers = [
        {'name':'John Doe', 
         'email': 'johndoe@gmail.com',
         'phone': '1234567890'},
        {'name':'John Doe', 
         'email': 'johndoe@gmail.com',
         'phone': '1234567890'},
        {'name':'John Doe', 
         'email': 'johndoe@gmail.com',
         'phone': '1234567890'},
         {'name':'John Doe', 
         'email': 'johndoe@gmail.com',
         'phone': '1234567890'},
         {'name':'John Doe', 
         'email': 'johndoe@gmail.com',
         'phone': '1234567890'}

    ]
    context = {'customers': customers}
    return render(request, 'customers.html', context)