# BROKEN
def add_item(item, cart=[]): # cart is a default argument 
    cart.append(item)
    return cart
 
# print("********** add_item_safe **********\n",add_item("apple"))      # ['apple']
# print(add_item("banana"))   # ['apple', 'banana']  <- unexpected!

# FIXED
def add_item_safe(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print("\n\n********** add_item_safe **********\n",add_item_safe("apple"))   
print(add_item_safe("banana")) 
print(add_item_safe("Orange")) 