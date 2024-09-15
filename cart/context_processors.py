from .cart import Cart

# cerate context processor so our cart work on all the pages on the app 
def cart(request):
    # Return the default data from our Cart
    return{'cart': Cart(request)}