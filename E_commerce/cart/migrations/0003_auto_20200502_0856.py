# Generated by Django 3.0.5 on 2020-05-02 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20200428_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='added_date',
            field=models.DateField(blank=True),
        ),
    ]
