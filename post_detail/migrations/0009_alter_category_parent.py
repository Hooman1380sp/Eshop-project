# Generated by Django 4.0.4 on 2022-06-05 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_detail', '0008_alter_information_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ManyToManyField(blank=True, to='post_detail.category'),
        ),
    ]
