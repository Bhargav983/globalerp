from django.shortcuts import render, redirect
from .models import Product

def products(request):
    if request.method == 'POST':
        # Get the form data from the request
        barcode = request.POST.get('barcode')
        product_name = request.POST.get('product_name')
        product_company = request.POST.get('product_company')
        category = request.POST.get('category')
        description = request.POST.get('description')
        stock_quantity = request.POST.get('stock_quantity')
        purchase_price = request.POST.get('purchase_price')
        sales_price = request.POST.get('sales_price')

        # Create a new product with the submitted data
        Product.objects.create(
            barcode=barcode,
            product_name=product_name,
            category=category,
            product_company=product_company,
            description=description,
            stock_quantity=stock_quantity,
            purchase_price=purchase_price,
            sales_price=sales_price
        )
    
    return render(request, 'products.html') 
