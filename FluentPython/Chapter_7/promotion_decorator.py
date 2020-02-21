promos = [] # The promos list starts empty.

def promotion(promo_func): # promotion decorator returns promo_func unchanged, after adding it to the promos list.
    promos.append(promo_func)
    return promo_func

@promotion # Any function decorated by @promotion will be added to promos.
def fidelity(order):
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def large_order(order):
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

def best_promo(order): # No changes needed to best_promos, because it relies on the promos list.
    """Select best discount available
    """
    return max(promo(order) for promo in promos)