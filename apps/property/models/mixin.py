from django.contrib.auth import get_user_model
from django.db import models

user_model = get_user_model()


class UserMixin(models.Model):
    user = models.ForeignKey(
        user_model, verbose_name="用户", on_delete=models.CASCADE
    )

    class Meta:
        abstract = True


class CreateMixin(models.Model):
    create_at = models.DateField(
        verbose_name="创建日期", db_index=True, auto_now_add=True
    )
    
    class Meta:
        abstract = True
