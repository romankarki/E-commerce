# Generated by Django 3.0.5 on 2020-04-28 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='added_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
