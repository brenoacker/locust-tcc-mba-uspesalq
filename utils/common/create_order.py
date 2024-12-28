from utils.enums.offer_type import OfferType


def calculate_total_price_with_discount(total_price, discount_type, discount_value):
    if discount_type == OfferType.PERCENTAGE.value:
        return total_price - (total_price * discount_value / 100)
    elif discount_type == OfferType.AMOUNT.value:
        if total_price < discount_value:
            return 0
        else:
            return total_price - discount_value