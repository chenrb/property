from django.db import models

from apps.property.constants import APP_NAME
from apps.property.models.mixin import UserMixin, CreateMixin


class DebitCard(UserMixin, CreateMixin):
    card_id = models.IntegerField(verbose_name="卡号")
    bank = models.CharField(verbose_name="银行", max_length=32)
    balance = models.DecimalField(
        verbose_name="余额", max_digits=10, decimal_places=2
    )

    class Meta:
        verbose_name = "借记卡"
        verbose_name_plural = "借记卡"

    def __str__(self):
        return "Debit({})".format(str(self.card_id)[-4:])


class MonetaryFund(UserMixin, CreateMixin):
    name = models.CharField(verbose_name="名字", max_length=64)
    balance = models.DecimalField(
        verbose_name="余额", max_digits=10, decimal_places=2
    )

    class Meta:
        verbose_name = "货币基金"
        verbose_name_plural = "货币基金"

    def __str__(self):
        return self.name


class AppBalance(UserMixin, CreateMixin):
    """应用余额，例如：支付宝余额、微信零钱"""
    app_name = models.PositiveSmallIntegerField(
        verbose_name="app名字", choices=APP_NAME
    )
    balance = models.DecimalField(
        verbose_name="余额", max_digits=10, decimal_places=2
    )

    class Meta:
        verbose_name = "应用余额"
        verbose_name_plural = "应用余额"

    def __str__(self):
        return self.get_app_name_display()


class Accumulation(UserMixin, CreateMixin):
    """公积金"""
    region = models.CharField(verbose_name="地区", max_length=16)
    balance = models.DecimalField(
        verbose_name="余额", max_digits=10, decimal_places=2
    )

    class Meta:
        verbose_name = "公积金"
        verbose_name_plural = "公积金"

    def __str__(self):
        return self.region
