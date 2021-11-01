# Generated by Django 3.2.8 on 2021-11-01 09:18

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estate_name', models.CharField(max_length=200, unique=True)),
                ('estate_logo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
