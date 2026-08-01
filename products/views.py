from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
def product_list(request):
    pass

def add_product(request):
    pass

def edit_product(request, product_id):
    pass

def delete_product(request, product_id):
    pass

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ProductForm
from .models import Product
from farmers.models import Farmer


@login_required
def add_product(request):

    farmer = Farmer.objects.get(
        user=request.user
    )

    if request.method == 'POST':

        form = ProductForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            product = form.save(
                commit=False
            )

            product.farmer = farmer

            product.save()

            return redirect(
                'product_list'
            )

    else:

        form = ProductForm()

    return render(
        request,
        'products/add_product.html',
        {'form': form}
    )

@login_required
def product_list(request):

    farmer = Farmer.objects.get(
        user=request.user
    )

    products = Product.objects.filter(
        farmer=farmer
    )

    return render(
        request,
        'products/product_list.html',
        {
            'products': products
        }
    )
    
@login_required
def edit_product(request, product_id):

    farmer = Farmer.objects.get(
        user=request.user
    )

    product = get_object_or_404(
        Product,
        id=product_id,
        farmer=farmer
    )

    if request.method == 'POST':

        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product
        )

        if form.is_valid():

            form.save()

            return redirect(
                'product_list'
            )

    else:

        form = ProductForm(
            instance=product
        )

    return render(
        request,
        'products/edit_product.html',
        {
            'form': form
        }
    )
    
@login_required
def delete_product(request, product_id):

    farmer = Farmer.objects.get(
        user=request.user
    )

    product = get_object_or_404(
        Product,
        id=product_id,
        farmer=farmer
    )

    if request.method == 'POST':

        product.delete()

        return redirect(
            'product_list'
        )

    return render(
        request,
        'products/delete_product.html',
        {
            'product': product
        }
    )
    
def all_products(request):

    products = Product.objects.filter(
        is_available=True
    )

    return render(
        request,
        'products/all_products.html',
        {
            'products': products
        }
    )
    
def product_detail(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    return render(
        request,
        'products/product_detail.html',
        {
            'product': product
        }
    )