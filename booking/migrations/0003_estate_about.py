# Generated by Django 3.2.8 on 2021-11-01 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20211101_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='about',
            field=models.TextField(default=1, verbose_name='About Estate'),
            preserve_default=False,
        ),
    ]
