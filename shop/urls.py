"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sales.views import site_home, products_list, customers, orders, order_details
from accounts.views import login_page, signin, register_page, register
from django.contrib.auth import views as auth_views
from laptops.views import laptop_detail, laptop_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', site_home, name='home'),
    path('products', products_list, name='products'),
    path('customers', customers, name='customers'),
    path('orders/<int:customer_id>', orders, name='orders'),
    path('order_details/<int:order_id>', order_details, name='order_details'),

    path('login_page', login_page, name='login_page'),
    path('login', signin, name='login'),
    path('register_page', register_page, name='register_page'),
    path('register', register, name='register'),
    path('laptop_list', laptop_list, name='laptop_list'),    
    path('laptops/<int:laptop_id>', laptop_detail, name='laptop_detail'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
