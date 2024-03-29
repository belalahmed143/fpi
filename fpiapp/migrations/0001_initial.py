# Generated by Django 3.1.1 on 2020-10-05 08:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplaintForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='CoverCarousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('caro_img', models.ImageField(upload_to='Carousel-Picture')),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NoticeBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('file_up', models.FileField(upload_to='Notice file')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherStaffCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=50)),
                ('job_possition', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('image', models.ImageField(default='no_img.jpg', upload_to='Teachers staffs picture')),
                ('department_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fpiapp.teacherstaffcategory')),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birthday', models.DateTimeField(blank=True)),
                ('father_name', models.CharField(blank=True, max_length=30)),
                ('mother_name', models.CharField(blank=True, max_length=30)),
                ('phone', models.CharField(blank=True, max_length=15, unique=True)),
                ('permanent_address', models.CharField(blank=True, max_length=100)),
                ('present_address', models.CharField(blank=True, max_length=100)),
                ('department_name', models.CharField(blank=True, max_length=30)),
                ('session', models.CharField(blank=True, max_length=15)),
                ('roll_number', models.IntegerField(blank=True, unique=True)),
                ('registration_number', models.IntegerField(blank=True, unique=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_head_name', models.CharField(max_length=50)),
                ('dep_head_image', models.ImageField(default='no_img.jpg', upload_to="department of head's picture")),
                ('dep_head_message', models.TextField(max_length=1000)),
                ('dep_head_possition', models.CharField(max_length=50)),
                ('department_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fpiapp.departmentname')),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentCarousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caro_img', models.ImageField(upload_to='Department-Carousel-Picture')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fpiapp.departmentname')),
            ],
        ),
    ]
