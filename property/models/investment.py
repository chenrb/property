from django.db import models

from .mixin import UserMixin, CreateMixin


class StockAccount(UserMixin, CreateMixin):
    name = models.CharField(verbose_name="证券公司名称", max_length=8)
    number = models.CharField(verbose_name="账户号码", max_length=16)
    account = models.DecimalField(
        verbose_name="总额", max_digits=10, decimal_places=2
    )

    class Meta:
        verbose_name = "股票账户"
        verbose_name_plural = "股票账户"

    def __str__(self):
        return self.number
