class OfferPayload:

    def create_offer(id, discount_type, discount_value, expiration_days):
        return {
            "id": id,
            "discount_type": discount_type.value,
            "discount_value": discount_value,
            "expiration_days": expiration_days
        }