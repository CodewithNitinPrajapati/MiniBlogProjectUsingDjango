from django.urls import path
from . import views

urlpatterns =[
    path('',views.home , name='home'),
    path('Contact',views.Contact , name='Contact'),
    path('Dashboard',views.Dashboard , name='Dashboard'),
    path('Login',views.user_login , name='Login'),
    path('Logout',views.user_logout , name='Logout'),
    path('Signup',views.user_signup , name='Signup'),
    path('Dashboard',views.Dashboard , name='Dashboard'),
    path('About',views.About , name='About'),
    path('Updatepost<int:id>',views.Update_post , name='Updatepost'),
    path('Addpost',views.Add_post, name='Addpost'),
    path('Deletepost<int:id>',views.Delete_post, name='Deletepost'),
    path('detailcontact',views.detail_contact , name='detailcontact'),
    path('thanks',views.thanks , name='thanks'),
]
