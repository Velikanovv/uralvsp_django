# Generated by Django 3.2.4 on 2021-06-27 17:28

import catalog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20210625_1949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subproduct',
            options={'verbose_name': 'Модель продукта', 'verbose_name_plural': 'Модели продукта'},
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to=catalog.models.category_img_path, verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='category',
            name='text',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=catalog.models.product_img_path, verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.subcategory', verbose_name='ПодКатегория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='text',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='production',
            name='image',
            field=models.ImageField(upload_to=catalog.models.production_img_path, verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='production',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='productparam',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='productparam',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Нзвание'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to=catalog.models.service_img_path, verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(upload_to=catalog.models.subcategory_img_path, verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='text',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='subproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='subproduct',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]
