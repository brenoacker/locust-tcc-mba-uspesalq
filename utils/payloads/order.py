class OrderPayload:

    def create_order(cart_id, order_type, offer_id = 0):
        return {
          "type": order_type,
          "cart_id": cart_id,
          "offer_id": offer_id
        }