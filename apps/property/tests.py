from decimal import Decimal

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.property.constants import WECHAT
from apps.property.models import (
    Accumulation,
    AppBalance,
    CreditCard,
    DebitCard,
    MonetaryFund,
    StockAccount,
    Target,
)


class PropertyModelDisplayTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="tester",
            password="test-pass",
        )

    def test_debit_card_string_uses_last_four_digits(self):
        card = DebitCard(
            user=self.user,
            card_id=12345678,
            bank="Test Bank",
            balance=Decimal("100.00"),
        )

        self.assertEqual(str(card), "Debit(5678)")

    def test_credit_card_string_uses_last_four_digits(self):
        card = CreditCard(
            user=self.user,
            card_id=87654321,
            bank="Test Bank",
            bill=Decimal("250.00"),
        )

        self.assertEqual(str(card), "Credit(4321)")

    def test_named_balance_models_use_visible_name_fields(self):
        fund = MonetaryFund(
            user=self.user,
            name="Cash Fund",
            balance=Decimal("10.00"),
        )
        accumulation = Accumulation(
            user=self.user,
            region="Shanghai",
            balance=Decimal("20.00"),
        )
        stock = StockAccount(
            user=self.user,
            name="Broker",
            number="A123",
            account=Decimal("30.00"),
        )
        target = Target(user=self.user, target=100000)

        self.assertEqual(str(fund), "Cash Fund")
        self.assertEqual(str(accumulation), "Shanghai")
        self.assertEqual(str(stock), "A123")
        self.assertEqual(str(target), "100000")

    def test_app_balance_string_uses_choice_display(self):
        balance = AppBalance(
            user=self.user,
            app_name=WECHAT,
            balance=Decimal("88.00"),
        )

        self.assertEqual(str(balance), "微信")


class PropertyAdminRegistrationTests(TestCase):
    def test_property_models_are_registered_with_admin_site(self):
        registered_models = admin.site._registry

        self.assertIn(Target, registered_models)
        self.assertIn(DebitCard, registered_models)
        self.assertIn(CreditCard, registered_models)
        self.assertIn(MonetaryFund, registered_models)
        self.assertIn(AppBalance, registered_models)
        self.assertIn(Accumulation, registered_models)
        self.assertIn(StockAccount, registered_models)
