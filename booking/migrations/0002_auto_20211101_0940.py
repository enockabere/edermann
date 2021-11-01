# Generated by Django 3.2.8 on 2021-11-01 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estate',
            old_name='estate_logo',
            new_name='logo',
        ),
        migrations.RemoveField(
            model_name='estate',
            name='estate_name',
        ),
        migrations.AddField(
            model_name='estate',
            name='name',
            field=models.CharField(default=1, max_length=200, unique=True, verbose_name='Estate Name'),
            preserve_default=False,
        ),
    ]
