from django.db import models

from apps.property.models.mixin import UserMixin, CreateMixin


class Target(UserMixin, CreateMixin):
    target = models.PositiveIntegerField(verbose_name="目标")
    is_finished = models.BooleanField(verbose_name="是否已完成", default=False)
    finish_at = models.DateField(verbose_name="完成日期", blank=True, null=True)

    class Meta:
        verbose_name = "目标"
        verbose_name_plural = "目标"

    def __str__(self):
        return str(self.target)
