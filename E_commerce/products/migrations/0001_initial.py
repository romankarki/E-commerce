# Generated by Django 3.0.5 on 2020-04-27 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('photo', models.ImageField(upload_to='product_pics')),
                ('category', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('in_stock', models.PositiveIntegerField()),
            ],
        ),
    ]
