from django.db import models

from apps.property.models.mixin import UserMixin, CreateMixin


class CreditCard(UserMixin, CreateMixin):
    card_id = models.IntegerField(verbose_name="卡号")
    bank = models.CharField(verbose_name="银行", max_length=32)
    bill = models.DecimalField(
        verbose_name="账单", max_digits=10, decimal_places=2
    )

    class Meta:
        verbose_name = "信用卡"
        verbose_name_plural = "信用卡"

    def __str__(self):
        return "Credit({})".format(str(self.card_id)[-4:])
