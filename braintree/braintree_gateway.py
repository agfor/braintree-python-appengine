from braintree.add_on_gateway import AddOnGateway
from braintree.address_gateway import AddressGateway
from braintree.client_token_gateway import ClientTokenGateway
from braintree.configuration import Configuration
from braintree.credit_card_gateway import CreditCardGateway
from braintree.customer_gateway import CustomerGateway
from braintree.discount_gateway import DiscountGateway
from braintree.merchant_account_gateway import MerchantAccountGateway
from braintree.merchant_gateway import MerchantGateway
from braintree.oauth_gateway import OAuthGateway
from braintree.paypal_account_gateway import PayPalAccountGateway
from braintree.payment_method_gateway import PaymentMethodGateway
from braintree.payment_method_nonce_gateway import PaymentMethodNonceGateway
from braintree.plan_gateway import PlanGateway
from braintree.settlement_batch_summary_gateway import SettlementBatchSummaryGateway
from braintree.subscription_gateway import SubscriptionGateway
from braintree.testing_gateway import TestingGateway
from braintree.transaction_gateway import TransactionGateway
from braintree.transparent_redirect_gateway import TransparentRedirectGateway
from braintree.credit_card_verification_gateway import CreditCardVerificationGateway
from braintree.webhook_notification_gateway import WebhookNotificationGateway
from braintree.webhook_testing_gateway import WebhookTestingGateway
import braintree.configuration

class BraintreeGateway(object):
    def __init__(self, config=None, **kwargs):
        if isinstance(config, braintree.configuration.Configuration):
            self.config = config
        else:
            self.config = Configuration(
                client_id=kwargs.get("client_id"),
                client_secret=kwargs.get("client_secret"),
                access_token=kwargs.get("access_token"),
                http_strategy=kwargs.get("http_strategy")
            )
        self.add_on = AddOnGateway(self)
        self.address = AddressGateway(self)
        self.client_token = ClientTokenGateway(self)
        self.credit_card = CreditCardGateway(self)
        self.customer = CustomerGateway(self)
        self.discount = DiscountGateway(self)
        self.merchant_account = MerchantAccountGateway(self)
        self.merchant = MerchantGateway(self)
        self.oauth = OAuthGateway(self)
        self.plan = PlanGateway(self)
        self.settlement_batch_summary = SettlementBatchSummaryGateway(self)
        self.subscription = SubscriptionGateway(self)
        self.transaction = TransactionGateway(self)
        self.transparent_redirect = TransparentRedirectGateway(self)
        self.verification = CreditCardVerificationGateway(self)
        self.webhook_notification = WebhookNotificationGateway(self)
        self.webhook_testing = WebhookTestingGateway(self)
        self.payment_method = PaymentMethodGateway(self)
        self.payment_method_nonce = PaymentMethodNonceGateway(self)
        self.paypal_account = PayPalAccountGateway(self)
        self.testing = TestingGateway(self)
