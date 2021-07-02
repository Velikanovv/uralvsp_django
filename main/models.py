from django.db import models
from django.utils import timezone
# Create your models here.

class FeedBack(models.Model):
    text = models.CharField(verbose_name='Номер телефона или почта',null=False, blank=True, max_length=500, default="Ошибка")
    date = models.DateTimeField(verbose_name='Дата',default=timezone.now, blank=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Заявка на обратную связь'
        verbose_name_plural = 'Заявки на обратную связь'

class Application(models.Model):
    name = models.CharField(verbose_name='Имя',null=False, blank=True, max_length=500, default="Ошибка")
    email = models.CharField(verbose_name='Почта',null=False, blank=True, max_length=500, default="Ошибка")
    phone = models.CharField(verbose_name='Номер телефона',null=False, blank=True, max_length=500, default="Ошибка")
    text = models.TextField(verbose_name='Обращение')
    date = models.DateTimeField(verbose_name='Дата', default=timezone.now, blank=True)

    help = models.CharField(verbose_name='Страница',null=False, blank=True, max_length=500, default="Ошибка")

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'