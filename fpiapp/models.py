from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE, max_length=1)
    image               = models.ImageField(upload_to="profile picture", default='no_img.jpg')
    date_of_birthday    = models.DateField(auto_now_add=False,blank=True,null=True)
    father_name         = models.CharField(max_length=30,blank=True,null=True)
    mother_name         = models.CharField(max_length=30,blank=True,null=True)
    phone               = models.CharField(max_length=15,unique=True,blank=True,null=True)
    permanent_address   = models.CharField(max_length=100,blank=True,null=True)
    present_address     = models.CharField(max_length=100,blank=True,null=True)
    department_name     = models.CharField(max_length=30,blank=True,null=True)



    def __str__(self):
        return self.user.username

        
class CoverCarousel(models.Model):
    name                = models.CharField(max_length=100)
    caro_img            = models.ImageField(upload_to='Carousel-Picture')

    def __str__(self):
        return self.name

class DepartmentName(models.Model):
    name                = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class DepartmentCarousel(models.Model):
    name                    = models.ForeignKey(DepartmentName, on_delete=models.CASCADE)
    caro_img                = models.ImageField(upload_to='Department-Carousel-Picture')

    def __str__(self):
        return self.name.name

class DepartmentDetail(models.Model):
    department_name         = models.ForeignKey(DepartmentName, on_delete=models.CASCADE)
    dep_head_name           = models.CharField(max_length=50)
    dep_head_image          = models.ImageField(upload_to="department of head's picture", default='no_img.jpg')
    dep_head_message        = models.TextField(max_length=1000)
    dep_head_possition      = models.CharField(max_length=50 )
    
    
    def __str__(self):
        return self.department_name.name

class TeacherStaffCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class TeacherStaff(models.Model):
    teacher_name        =models.CharField(max_length=50)
    department_name     = models.ForeignKey(TeacherStaffCategory,on_delete=models.CASCADE)
    job_possition       = models.CharField(max_length=50)
    phone               =models.CharField(max_length=15)
    image               = models.ImageField(upload_to="Teachers staffs picture", default='no_img.jpg')

    def __str__(self):
        return self.teacher_name +" "+self.department_name.name

class NoticeBoard(models.Model):
    title               = models.CharField(max_length=100)
    description         = models.TextField( blank=True)
    file_up             = models.FileField(upload_to="Notice file")
    upload_date         = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name +" "+self.email

class Complaint(models.Model):
    subject             = models.CharField(max_length=50)
    description         = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.subject

class Gallery(models.Model):
    title =models.CharField(max_length=50)
    image = models.ImageField(upload_to='gallary')
    caption = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title