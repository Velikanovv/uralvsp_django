# Generated by Django 3.2.4 on 2021-06-25 10:19

from django.db import migrations, models
import django.utils.timezone
import news.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=news.models.news_img_path)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('text', models.TextField()),
            ],
        ),
    ]
