class PaymentPayload:

    def execute_payment(payment_method, payment_card_gateway):
        return {
          "payment_method": payment_method,
          "payment_card_gateway": payment_card_gateway
        }