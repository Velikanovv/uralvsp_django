# Generated by Django 3.2.4 on 2021-07-02 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0012_alter_page_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.CharField(blank=True, max_length=100, unique=True, verbose_name='Ссылка'),
        ),
    ]
