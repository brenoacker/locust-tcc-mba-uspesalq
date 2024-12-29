


# from tests.create_user.create_young_user import CreateYoungUserTest

# from tests.create_user.create_senior_user import CreateSeniorUserTest

# from tests.create_user.create_mid_age_user import CreateMidAgeUserTest

# from tests.data_creation.create_offer.create_amount_offer import CreateAmountOfferTest

# from tests.data_creation.create_product.create_burger import CreateBurgerTest

# from tests.data_creation.create_product.create_dessert import CreateDessertTest

# from tests.data_creation.create_product.create_drink import CreateDrinkTest

# from tests.data_creation.create_product.create_side_dish import CreateSideDishTest


# from tests.order.delivery_order_senior_user_with_offer_and_card import DeliveryOrderSeniorUserWithOfferAndCard


# from tests.order.delivery_order_senior_user_without_offer_and_card import DeliveryOrderSeniorUserWithoutOfferAndCard

# from tests.order.delivery_order_senior_user_with_offer_and_card import DeliveryOrderSeniorUserWithOfferAndCard

# from tests.order.delivery.delivery_order_senior_user_without_offer_and_cash import DeliveryOrderSeniorUserWithoutOfferAndCash

# from tests.data_creation.create_user.create_senior_user import CreateSeniorUserTest

from tests.data_creation.create_offer.create_amount_offer import \
    CreateAmountOfferTest
from tests.data_creation.create_product.create_burger import CreateBurgerTest
from tests.data_creation.create_product.create_dessert import CreateDessertTest
from tests.data_creation.create_product.create_drink import CreateDrinkTest
from tests.data_creation.create_product.create_side_dish import \
    CreateSideDishTest
from tests.data_creation.create_user.create_mid_age_user import \
    CreateMidAgeUserTest
from tests.data_creation.create_user.create_senior_user import \
    CreateSeniorUserTest
from tests.data_creation.create_user.create_young_user import \
    CreateYoungUserTest
from tests.order.delivery.delivery_order_mid_age_user_with_offer_and_card import \
    DeliveryOrderMidAgeUserWithOfferAndCard
from tests.order.delivery.delivery_order_mid_age_user_with_offer_and_cash import \
    DeliveryOrderMidAgeUserWithOfferAndCash
from tests.order.delivery.delivery_order_mid_age_user_without_offer_and_card import \
    DeliveryOrderMidAgeUserWithoutOfferAndCard
from tests.order.delivery.delivery_order_mid_age_user_without_offer_and_cash import \
    DeliveryOrderMidAgeUserWithoutOfferAndCash
from tests.order.delivery.delivery_order_senior_user_with_offer_and_card import \
    DeliveryOrderSeniorUserWithOfferAndCard
from tests.order.delivery.delivery_order_senior_user_with_offer_and_cash import \
    DeliveryOrderSeniorUserWithOfferAndCash
from tests.order.delivery.delivery_order_senior_user_without_offer_and_card import \
    DeliveryOrderSeniorUserWithoutOfferAndCard
from tests.order.delivery.delivery_order_senior_user_without_offer_and_cash import \
    DeliveryOrderSeniorUserWithoutOfferAndCash
from tests.order.drive_thru.drive_thru_order_senior_user_with_offer_and_card import \
    DriveThruOrderSeniorUserWithOfferAndCard
from tests.order.drive_thru.drive_thru_order_senior_user_with_offer_and_cash import \
    DriveThruOrderSeniorUserWithOfferAndCash
from tests.order.drive_thru.drive_thru_order_senior_user_without_offer_and_card import \
    DriveThruOrderSeniorUserWithoutOfferAndCard
from tests.order.drive_thru.drive_thru_order_senior_user_without_offer_and_cash import \
    DriveThruOrderSeniorUserWithoutOfferAndCash
from tests.order.in_store.in_store_order_senior_user_with_offer_and_card import \
    InStoreOrderSeniorUserWithOfferAndCard
from tests.order.in_store.in_store_order_senior_user_with_offer_and_cash import \
    InStoreOrderSeniorUserWithOfferAndCash
from tests.order.in_store.in_store_order_senior_user_without_offer_and_card import \
    InStoreOrderSeniorUserWithoutOfferAndCard
from tests.order.in_store.in_store_order_senior_user_without_offer_and_cash import \
    InStoreOrderSeniorUserWithoutOfferAndCash


class FeaturesWeight():

    @staticmethod
    def get_features_weight():

        tasks = []

        # tasks.append((CreateYoungUserTest, 1))
        # tasks.append((CreateSeniorUserTest, 1))
        # tasks.append((CreateMidAgeUserTest, 1))

        # tasks.append((CreateAmountOfferTest, 1))

        # tasks.append((CreateBurgerTest, 1))
        # tasks.append((CreateDessertTest, 1))
        # tasks.append((CreateDrinkTest, 1))
        # tasks.append((CreateSideDishTest, 1))

        # tasks.append((DeliveryOrderSeniorUserWithOfferAndCard, 11))
        # tasks.append((DeliveryOrderSeniorUserWithoutOfferAndCard, 5))
        # tasks.append((DeliveryOrderSeniorUserWithoutOfferAndCash, 5))
        # tasks.append((DeliveryOrderSeniorUserWithOfferAndCash, 11))

        tasks.append((DeliveryOrderMidAgeUserWithOfferAndCard, 11))
        tasks.append((DeliveryOrderMidAgeUserWithoutOfferAndCard, 5))
        tasks.append((DeliveryOrderMidAgeUserWithoutOfferAndCash, 5))
        tasks.append((DeliveryOrderMidAgeUserWithOfferAndCash, 11))

        # tasks.append((DriveThruOrderSeniorUserWithOfferAndCard, 11))
        # tasks.append((DriveThruOrderSeniorUserWithoutOfferAndCard, 5))
        # tasks.append((DriveThruOrderSeniorUserWithoutOfferAndCash, 5))
        # tasks.append((DriveThruOrderSeniorUserWithOfferAndCash, 11))

        # tasks.append((InStoreOrderSeniorUserWithOfferAndCard, 11))
        # tasks.append((InStoreOrderSeniorUserWithoutOfferAndCard, 5))
        # tasks.append((InStoreOrderSeniorUserWithoutOfferAndCash, 5))
        # tasks.append((InStoreOrderSeniorUserWithOfferAndCash, 11))

        return dict(tasks)