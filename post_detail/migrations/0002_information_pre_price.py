# Generated by Django 4.0.4 on 2022-05-14 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_detail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='pre_price',
            field=models.CharField(max_length=100, null=True),
        ),
    ]