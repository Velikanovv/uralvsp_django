from django.db import models
from django.utils import timezone
# Create your models here.

def news_img_path(instance, filename):
    return 'news/%s/img/%s' % (str(instance.pk), filename)

class News(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100, null=False, blank=False)
    image = models.ImageField(verbose_name='Фото',null=False, blank=False, upload_to=news_img_path, default='news/default.jpg')
    date = models.DateTimeField(verbose_name='Дата',default=timezone.now, null=False, blank=False, editable=False)
    short_text = models.TextField(verbose_name='Краткое описание',help_text="Будет показываться в списке новостей")
    text = models.TextField(verbose_name='Текст Новости')

    def __str__(self):
        return str(self.title) + '(' + str(self.date.date()) + ')'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
