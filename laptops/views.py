# views.py
from django.shortcuts import render, get_object_or_404
from .models import Laptop

def laptop_list(request):
    laptops = Laptop.objects.all()
    context = {'laptops': laptops}
    return render(request, 'laptop_list.html', context)

def laptop_detail(request, laptop_id):
    laptop = get_object_or_404(Laptop, pk=laptop_id)
    context = {'laptop': laptop}
    return render(request, 'laptop_detail.html', context)
