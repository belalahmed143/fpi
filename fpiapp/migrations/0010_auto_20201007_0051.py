# Generated by Django 3.1.1 on 2020-10-06 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fpiapp', '0009_auto_20201007_0015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='registration_number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='roll_number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='session',
        ),
    ]
