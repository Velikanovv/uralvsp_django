# Generated by Django 3.2.4 on 2021-06-25 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_auto_20210625_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pssettings',
            name='production_text',
            field=models.TextField(blank=True, help_text='Текст - Производство', null=True),
        ),
    ]
