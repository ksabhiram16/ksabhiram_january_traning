def add_order(order_id, orders=None):
    """
    Stores order IDs across multiple calls safely
    using a mutable list initialized inside the function.
    """
    if orders is None:
        orders = []

    orders.append(order_id)
    return orders



print(add_order(101))
print(add_order(102))
print(add_order(103))
