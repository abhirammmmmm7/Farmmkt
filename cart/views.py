from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from products.models import Product
from customers.models import Customer
from django.contrib.auth.decorators import login_required


@login_required
def add_to_cart(request, product_id):

    customer = Customer.objects.get(
        user=request.user
    )

    cart, created = Cart.objects.get_or_create(
        customer=customer
    )

    product = get_object_or_404(
        Product,
        id=product_id
    )

    quantity = int(request.POST.get('quantity', 1))

    item, created = CartItem.objects.get_or_create(cart=cart,product=product)

    if created:

        item.quantity = quantity

    else:

        item.quantity += quantity

    item.save()
    
    if not created:
        item.quantity += 1
        item.save()

    return redirect('cart')


@login_required
def cart_view(request):

    customer = Customer.objects.get(
        user=request.user
    )

    cart, created = Cart.objects.get_or_create(
        customer=customer
    )

    total = sum(
        item.total_price
        for item in cart.items.all()
    )

    return render(
        request,
        'cart/cart.html',
        {
            'cart': cart,
            'total': total
        }
    )


@login_required
def remove_from_cart(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id
    )

    item.delete()

    return redirect('cart')