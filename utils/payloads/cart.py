from typing import List

from cart_entity import CartItemEntity


class CartPayload:

    def create_cart(cart_items: List[CartItemEntity]):
        
        cart_items_payload = []
        
        for cart_item in cart_items:
            cart_items_payload.append({
                "product_id": cart_item.product_id,
                "quantity": cart_item.quantity
            })

        return {
            "items": cart_items_payload
        }