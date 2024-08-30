from django.db import models

from auth_data.models import Login

class Message(models.Model):
    """Модель для хранения сообщений."""

    owner = models.ForeignKey(
        Login,
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name='Владелец')
    theme = models.CharField(
        verbose_name='Тема',
        max_length=100,
    )
    send_date = models.DateTimeField(
        verbose_name='Дата отправки',
    )
    receipt_date = models.DateTimeField(
        verbose_name='Дата получения',
    )
    text = models.TextField(verbose_name='Текст сообщения')
    attachments_list = models.TextField(verbose_name='Список вложений')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.theme
