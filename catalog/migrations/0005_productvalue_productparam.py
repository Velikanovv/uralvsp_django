# Generated by Django 3.2.4 on 2021-06-25 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20210625_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvalue',
            name='productparam',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalog.productparam'),
            preserve_default=False,
        ),
    ]
