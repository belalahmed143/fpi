# Generated by Django 3.1.1 on 2020-10-07 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpiapp', '0011_auto_20201007_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='gallary')),
                ('caption', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
