# Generated by Django 4.0.4 on 2023-04-26 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_detail', '0012_information_is_active_information_is_delete'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='information',
            options={'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterField(
            model_name='information',
            name='slug',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
