# Generated by Django 3.2.4 on 2021-06-27 17:28

from django.db import migrations, models
import django.utils.timezone
import news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_short_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to=news.models.news_img_path, verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='news',
            name='short_text',
            field=models.TextField(help_text='Будет показываться в списке новостей', verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=models.TextField(verbose_name='Текст Новости'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]
