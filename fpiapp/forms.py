from django import forms
from django.contrib.auth.forms import UserCreationForm,User
from django.core.exceptions import ValidationError
from .models import Profile


Dep_Name =(
    ('s','select-department'),
    ('Computer','Computer'),
    ('Electical','Electical'),
    ('Civil','Civil'),
    ('Mechanical','Mechanical'),
    ('Powar','Powar'),
    ('R&AC','R&AC'),

)


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,
               widget=forms.TextInput(attrs={
                   "class":"form-control",
                   "placeholder":"Enter your first name.."
               }) 
               )
    last_name = forms.CharField(max_length=30,
            widget=forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Enter your second name.."
            }) 
            )
    username = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Enter your username.."
        }) 
        )
    email = forms.EmailField(
            widget=forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Enter your email.."
            }) 
            )
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email Already Exists')
        return email
    class Meta:
        model=User
        fields =[ 'username', 'first_name', 'last_name', 'email']



class UpdateRegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields =[ 'username', 'first_name', 'last_name', 'email']

class UpdateProfileForm(forms.ModelForm):
    department_name     = forms.CharField(max_length=10,widget=forms.Select(choices= Dep_Name),required=True)
    class Meta:
        model = Profile
        fields = ['image','father_name','mother_name','date_of_birthday','phone','department_name','permanent_address','present_address']



# class StudentRegisterForm(UserCreationForm):
#     first_name          = forms.CharField(required=True)
#     last_name           = forms.CharField(required=True)
#     date_of_birthday    = forms.DateTimeField(required=True)
#     father_name         = forms.CharField(required=True)
#     mother_name         = forms.CharField(required=True)
#     email               = forms.EmailField(required=True)
#     phone               = forms.CharField(required=True)
#     permanent_address   = forms.CharField(required=True)
#     present_address     = forms.CharField(required=True)
#     department_name     = forms.CharField(max_length=10,widget=forms.Select(choices= Dep_Name),required=True)
#     session             = forms.CharField(required=True)
#     roll_number         = forms.IntegerField(required=True)
#     registration_number = forms.IntegerField(required=True)




















# # from django.core.exceptions import ValidationError

# # # class StudentRegForm(forms.ModelForm):
# # #     # def clean_email(self):
# # #     #     email = self.cleaned_data['email']
# # #     #     if StudentReg.objects.filter(email=email).exists():
# # #     #         raise ValidationError('Email Already Exists')
# # #     #     return email
# # #     class Meta:
# # #         model = StudentReg
# # #         fields ='__all__'



# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from fpiapp.models import User,Customer,Employee
# from django.db import transaction

# class CustomerSignupForm(UserCreationForm):
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(required=True)
#     phone_number = forms.CharField(required=True)

#     class Meta(UserCreationForm.Meta):
#         model = User

#     @transaction.atomic
#     def data_save(self):
#         user = super().save(commit=False)
#         user.first_name = self.changed_data.get('first_name')
#         user.last_name = self.changed_data.get('last_name')
#         user.save()
#         customer = Customer.objects.create(user=user)
#         customer.phone_number = self.changed_data.get('phone_number')
#         customer.save()
#         return customer



# class EmployeeSignupForm(UserCreationForm):
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(required=True)
#     phone_number = forms.CharField(required=True)

#     class Meta(UserCreationForm.Meta):
#         model = User

#     @transaction.atomic
#     def data_save(self):
#         user = super().save(commit=False)
#         user.first_name = self.changed_data.get('first_name')
#         user.last_name = self.changed_data.get('last_name')
#         user.save()
#         employee = Employee.objects.create(user=user)
#         employee.phone_number = self.changed_data.get('phone_number')
#         employee.designation = self.changed_data.get('designation')
#         employee.save()
#         return employee