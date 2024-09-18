from  myapp.models import Item


class Cart():
    def __init__(self, request):
        self.session = request.session

        # Get the current session cart if it exists
        cart = self.session.get('session_key')

        # If no cart exists, create an empty one
        if not cart:
            cart = self.session['session_key'] = {}

        # Make the cart available on all pages
        self.cart = cart  # Move this outside the if block

    def add(self, item, quantity):
        item_id = str(item.id)
        item_qty = str(quantity)
        # Logic for adding item to the cart
        if item_id not in self.cart:
            #self.cart[item_id] = {'price': str(item.price)}
             self.cart[item_id] = int(item_qty)


        # Mark the session as modified so the changes are saved
        self.session.modified = True
    def __len__(self):
        return len(self.cart)

    def get_items(self):
        # get ides from cart 
        item_ids = self.cart.keys()
        # Use ides to lookup items in database model
        items = Item.objects.filter(id__in=item_ids)
        # Return those looked up items
        return items
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    def update(self, item, quantity):
        item_id = str(item)
        item_qty = int(quantity)
        # Get the cart:
        ourcart = self.cart
        # Update the cart dictionary
        ourcart[item_id] = item_qty

        self.session.modified = True

        thing = self.cart
        return thing

         
    def delete(self, item):
        item_id = str(item)
     # Delete from dictionary cart
        if item_id in self.cart:
            del self.cart[item_id]

        self.session.modified = True

    def cart_total(self):
        # Get items ides 
        item_ides = self.cart.keys()
        # look up those keys in our items database model :
        items = Item.objects.filter(id__in=item_ides)
        # Qet quantities
        quantities = self.cart
        # Start counting at 0
        total = 0
        for key, value in quantities.items():
            # Convert key string into int so we can calculate 
            key = int(key)
            for item in items:
                if item.id == key:
                    total = total + (item.price * value)
        return total
