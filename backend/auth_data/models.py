from django.db import models


class Login(models.Model):
    """Модель для хранения логинов и паролей от почты."""

    login = models.CharField(
        verbose_name='Логин',
        unique=True,
        max_length=255,
    )
    password = models.CharField(
        verbose_name='Пароль',
        max_length=255,
    )

    class Meta:
        verbose_name = 'Логин'
        verbose_name_plural = 'Логины'

    def __str__(self):
        return self.login