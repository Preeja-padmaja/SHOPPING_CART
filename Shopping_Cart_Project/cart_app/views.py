from django.shortcuts import render, redirect, get_object_or_404
from Shopping_Cart_App.models import product_table
from cart_app.models import cart_table , cart_item_table
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart
def add_cart(request,product_id):
    product=product_table.objects.get(id=product_id)
    try:
        cart=cart_table.objects.get(cart_id=_cart_id(request))
    except cart_table.DoesNotExist:
        cart=cart_table.objects.create(cart_id=_cart_id(request))
        cart.save()
    try:
        cart_item=cart_item_table.objects.get(product=product,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except cart_item_table.DoesNotExist:
        cart_item=cart_item_table.objects.create(product=product,quantity=1,cart=cart)
        cart_item.save()
    return redirect('cart_app:cart_detail')
def cart_detail(request,total=0,counter=0,cart_items=None):
    try:
        cart=cart_table.objects.get(cart_id=_cart_id(request))
        cart_items=cart_item_table.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            total+=(cart_item.product.price * cart_item.quantity)
            counter+=cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))

def cart_remove(request,product_id):
    cart=cart_table.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(product_table,id=product_id)
    cart_item=cart_item_table.objects.get(product=product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_app:cart_detail')

def full_remove(request,product_id):
    cart = cart_table.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(product_table, id=product_id)
    cart_item = cart_item_table.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart_app:cart_detail')