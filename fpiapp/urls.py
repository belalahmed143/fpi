from django.urls import path
from .import views
from .views import Login
from fpiapp import views as user_views

urlpatterns = [
    path('', views.index, name='index'),
    path('gallary',views.gallary, name='gallary'),
    path("register/",user_views.register, name="register"),
    path("logout/", views.Logout, name="logout"),
    path("login/", Login.as_view(), name="login"),
    path('profile/', user_views.profile, name='profile'),  
    path('profile/update', user_views.profileupdate, name='profile-update'),
    
    path('notice/search/',views.NoticeSearch, name='notice-search'),
    # Dropdown menu with category
    path('TeacherStaffs/<name>/',views.TeacherStaffs, name='TeacherStaffs'),
    path('DepartmentDetails/<name>/',views.DepartmentDetails, name='DepartmentDetails'),
    path('contact',views.contact,name='contact')

]
