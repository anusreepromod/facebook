# Generated by Django 3.2.5 on 2021-10-07 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebookapp', '0013_sample3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample3',
            name='contact',
            field=models.BigIntegerField(),
        ),
    ]
