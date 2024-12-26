class ProductPayload:

    def create_product(product_id, product_name, product_price, product_category):
        return {
            "id": product_id,
            "name": product_name,
            "price": product_price,
            "category": product_category.value
        }