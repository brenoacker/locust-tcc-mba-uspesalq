class CartItemEntity:
    product_id: int
    quantity: int

    def __init__(self, product_id: int, quantity: int):
        self.product_id = product_id
        self.quantity = quantity