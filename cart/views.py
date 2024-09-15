from django.shortcuts import redirect, render, get_object_or_404
from .cart import Cart
from myapp.models import Item
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    # GEt the cart 
    cart = Cart(request)
    cart_items = cart.get_items
    quantities = cart.get_quants
    totals = cart.cart_total()

    return render(request, 'cart/cart_summary.html', {"cart_items":cart_items, 'quantities':quantities, 'totals':totals})

def cart_add(request):
    #get the cart
    cart = Cart(request)

    # Test for post
    if request.POST.get('action') == 'post':
        #get stuff 
        item_id = int(request.POST.get('item_id'))
        item_qty = int(request.POST.get('item_qty'))
        #lookup item in database 
        item = get_object_or_404(Item, id=item_id)
        #save to session 
        cart.add(item=item, quantity= item_qty)

        # Get cart Quantity
        cart_quantity = cart.__len__()

        # Return response
        #response = JsonResponse({'Item Name:': item.name})
        response = JsonResponse({'qty': cart_quantity})

        return response

    

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get stuff
        item_id = int(request.POST.get('item_id'))
        # Call delete function in Cart
        cart.delete(item=item_id)
        response = JsonResponse({'item':item_id})
        return response
        #return redirect('cart_summary')


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get stuff
        item_id = int(request.POST.get('item_id'))
        item_qty = int(request.POST.get('item_qty'))
        cart.update(item=item_id, quantity=item_qty)
        response = JsonResponse({'qty':item_qty})
        return response
        #return redirect('cart_summary')
