from django.contrib import admin

from .models import (
    Target,
    CreditCard,
    DebitCard,
    MonetaryFund,
    AppBalance,
    Accumulation,
    StockAccount
)


# Register your models here.
class TargetAdmin(admin.ModelAdmin):
    pass


class DebitCardAdmin(admin.ModelAdmin):
    list_display = ("card_id", "bank", "balance",)


class CreditCardAdmin(admin.ModelAdmin):
    list_display = ("card_id", "bank", "bill",)


class MonetaryFundAdmin(admin.ModelAdmin):
    list_display = ("name", "balance",)


class AppBalanceAdmin(admin.ModelAdmin):
    list_display = ("app_name", "balance",)


class AccumulationAdmin(admin.ModelAdmin):
    list_display = ("region", "balance",)


class StockAccountAdmin(admin.ModelAdmin):
    list_display = ("name", "number", "account",)


admin.site.register(Target, TargetAdmin)
admin.site.register(DebitCard, DebitCardAdmin)
admin.site.register(CreditCard, CreditCardAdmin)
admin.site.register(MonetaryFund, MonetaryFundAdmin)
admin.site.register(AppBalance, AppBalanceAdmin)
admin.site.register(Accumulation, AccumulationAdmin)
admin.site.register(StockAccount, StockAccountAdmin)
