


# from tests.create_user.create_young_user import CreateYoungUserTest

# from tests.create_user.create_senior_user import CreateSeniorUserTest

# from tests.create_user.create_mid_age_user import CreateMidAgeUserTest

# from tests.data_creation.create_offer.create_amount_offer import CreateAmountOfferTest

# from tests.data_creation.create_product.create_burger import CreateBurgerTest

# from tests.data_creation.create_product.create_dessert import CreateDessertTest

# from tests.data_creation.create_product.create_drink import CreateDrinkTest

# from tests.data_creation.create_product.create_side_dish import CreateSideDishTest


from tests.order.delivery_order_senior_user_with_offer import DeliveryOrderSeniorUserWithOffer


class FeaturesWeight():

    @staticmethod
    def get_features_weight():

        tasks = []

        # tasks.append((CreateYoungUserTest, 1))
        # tasks.append((CreateSeniorUserTest, 3))
        # tasks.append((CreateMidAgeUserTest, 1))

        # tasks.append((CreateAmountOfferTest, 1))

        # tasks.append((CreateBurgerTest, 1))
        # tasks.append((CreateDessertTest, 1))
        # tasks.append((CreateDrinkTest, 1))
        # tasks.append((CreateSideDishTest, 1))

        tasks.append((DeliveryOrderSeniorUserWithOffer, 1))

        return dict(tasks)