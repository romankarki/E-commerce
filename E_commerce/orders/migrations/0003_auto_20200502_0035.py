# Generated by Django 3.0.5 on 2020-05-02 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200501_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateField(auto_now=True),
        ),
    ]