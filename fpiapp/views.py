from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import *
from django.views.generic import DetailView
from .forms import *
from django.db.models import Q
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth import  authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    depnames = DepartmentName.objects.all()
    teacherstaffcategory =TeacherStaffCategory.objects.all()
    carousels = CoverCarousel.objects.all()
    noticeboard = NoticeBoard.objects.all()
    gallary =Gallery.objects.all().order_by('-date')[:8]

# Complaint Submit

    if request.method == 'POST':
        subject = request.POST['subject']
        description = request.POST['description']
        submit = Complaint(subject=subject,description=description)
        messages.success(request, f'Successfully Submit')
        submit.save()


    context ={
        "carousels":carousels,
        "noticeboard":noticeboard,
        'depnames': depnames,
        'teacherstaffcategory': teacherstaffcategory,
        'gallary':gallary
    }
    return render(request,'index.html', context)

#notice search
def gallary(request):
    noticeboard = NoticeBoard.objects.all()
    depnames = DepartmentName.objects.all()
    teacherstaffcategory =TeacherStaffCategory.objects.all()
    gallarios =Gallery.objects.all().order_by('-date')

    context={
        "noticeboard":noticeboard,
        'depnames': depnames,
        'teacherstaffcategory': teacherstaffcategory,
        'gallarios':gallarios,

    }
    return render(request, 'gallary.html',context)

def NoticeSearch(request):
    teacherstaffcategory =TeacherStaffCategory.objects.all()
    depnames = DepartmentName.objects.all()
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')
        
        if query is not None:
            lookups= Q(title__icontains=query)
            post= NoticeBoard.objects.filter(lookups).distinct()

            context ={
                'post':post,
                'submitbutton':submitbutton,
                'depnames':depnames,
                'teacherstaffcategory': teacherstaffcategory
            }
            return render(request,'noticesearch.html', context)
        else:
            return render(request, 'noticesearch.html')
    else:
        return render(request, 'noticesearch.html')



       
def TeacherStaffs(request, name):
    noticeboard = NoticeBoard.objects.all()
    teacherstaffcategory =TeacherStaffCategory.objects.all()
    depnames = DepartmentName.objects.all()

    # teachers_staffs
    cat = get_object_or_404(TeacherStaffCategory,name=name)
    teachers_staffs =TeacherStaff.objects.filter(department_name=cat.id)
    teacher_staff =TeacherStaff.objects.filter(department_name=cat.id)[:1]


    context={
        "noticeboard":noticeboard,
        'teacherstaffcategory':teacherstaffcategory,
        'depnames':depnames,
        'teachers_staffs':teachers_staffs,
        'teacher_staff':teacher_staff,
         'cat':cat
    }
    return render(request,'TeacherStaff.html',context)


def DepartmentDetails(request, name):
    noticeboard = NoticeBoard.objects.all()
    depnames = DepartmentName.objects.all()
    teacherstaffcategory =TeacherStaffCategory.objects.all()
    # details
    cat_dep_details =get_object_or_404(DepartmentName,name=name)
    dep_details =DepartmentDetail.objects.filter(department_name=cat_dep_details.id)

    #department carousel
    cat_dep_caro =get_object_or_404(DepartmentName,name=name)
    dep_caro =DepartmentCarousel.objects.filter(name=cat_dep_caro)

    context ={
        "noticeboard":noticeboard,
        'depnames':depnames,
        'teacherstaffcategory': teacherstaffcategory,

        'cat_dep_details':cat_dep_details,
        'dep_details':dep_details,

        'cat_dep_caro':cat_dep_caro,
        'dep_caro':dep_caro,
        

    }
    return render(request,'departmentdetails.html', context)


def contact(request):
    noticeboard = NoticeBoard.objects.all()    
    depnames = DepartmentName.objects.all()
    teacherstaffcategory =TeacherStaffCategory.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        submit = Contact(name=name,email=email,phone=phone,subject=subject,message=message)
        messages.success(request, f'Successfully Submit')
        submit.save()
    context={
        "noticeboard":noticeboard,
        'depnames':depnames,
        'teacherstaffcategory': teacherstaffcategory,
    }
    return render(request, 'contact.html',context)



def register(request):
    noticeboard = NoticeBoard.objects.all()
    depnames = DepartmentName.objects.all()
    teacherstaffcategory =TeacherStaffCategory.objects.all()
    if request.method =='POST':
        form =RegisterForm(request.POST)
        if form.is_valid():
            form.save()    
            messages.success(request,f'Account created for You are now able to login')
            return redirect('login')
    else:
        form =RegisterForm()
    context={
        "noticeboard":noticeboard,
        'depnames':depnames,
        'teacherstaffcategory':teacherstaffcategory,
        'form':form
    }
    return render(request, 'register.html',context)



class Login(View):
    def get(self,request):
        noticeboard = NoticeBoard.objects.all()
        depnames = DepartmentName.objects.all()
        teacherstaffcategory =TeacherStaffCategory.objects.all()

        context={
        "noticeboard":noticeboard,
        'depnames':depnames,
        'teacherstaffcategory':teacherstaffcategory,            
        }
        return render(request,'login.html',context)
    def post(self, request):
        username = request.POST.get('username')
        password =request.POST.get('password')

        submit = authenticate(request, username=username, password=password)

        if submit is not None:
            login(request, submit)
            return redirect('index')
        else:
            messages.warning(request, f'password or username incoret')

def Logout(request):
    logout(request)
    noticeboard = NoticeBoard.objects.all()
    depnames = DepartmentName.objects.all()
    teacherstaffcategory =TeacherStaffCategory.objects.all()

    context={
    "noticeboard":noticeboard,
    'depnames':depnames,
    'teacherstaffcategory':teacherstaffcategory,            
    }
    return render(request, 'logout.html',context)


@login_required
def profile(request):
    noticeboard = NoticeBoard.objects.all()
    depnames = DepartmentName.objects.all()
    teacherstaffcategory =TeacherStaffCategory.objects.all()

    context={
    "noticeboard":noticeboard,
    'depnames':depnames,
    'teacherstaffcategory':teacherstaffcategory,            
    }
    return render(request, 'profile.html',context)

@login_required
def profileupdate(request):
    noticeboard = NoticeBoard.objects.all()
    depnames = DepartmentName.objects.all()
    teacherstaffcategory =TeacherStaffCategory.objects.all()

    if request.method == 'POST':
        u_form = UpdateRegisterForm(request.POST, instance=request.user)
        p_form = UpdateProfileForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form =  UpdateRegisterForm(instance=request.user)
        p_form = UpdateProfileForm(instance=request.user.profile)

    context = {
        "noticeboard":noticeboard,
        'u_form': u_form,
        'p_form': p_form,
        'depnames':depnames,
        'teacherstaffcategory':teacherstaffcategory,  
    }

    return render(request, 'profileupdate.html', context)




