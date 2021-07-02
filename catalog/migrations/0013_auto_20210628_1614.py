# Generated by Django 3.2.4 on 2021-06-28 13:14

import catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20210628_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=catalog.models.product_img_path, verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='production',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=catalog.models.production_img_path, verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=catalog.models.service_img_path, verbose_name='Фото'),
        ),
    ]