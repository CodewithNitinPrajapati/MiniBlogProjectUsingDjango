from django.shortcuts import render , HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import SignupForm ,LoginForm ,PostForm
from django.contrib.auth.forms import  UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate , login , logout , update_session_auth_hash
from .models import Post,ContactModel
from django.contrib.auth.models import Group


def home(request):
    posts = Post.objects.all()
    return render(request,'Blog/home.html',{'posts':posts})


def About(request):
    return render(request,'Blog/about.html')


def Dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        print(request.user)
        full_name = user.get_full_name()
        print(user)
        print(full_name)
        gps = user.groups.all()
        return render(request,'Blog/dashboard.html',{'posts':posts ,'full_name':full_name,'groups':gps})
    else:
        return HttpResponseRedirect('Login')


def Contact(request):
    return render(request,'Blog/contact.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            #fm = AuthenticationForm(request=request , data=request.POST)   #iske liye form bna liya h 
            fm = LoginForm(request=request , data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname , password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request , 'Logged in successfully !!!')
                    return HttpResponseRedirect('Dashboard')        
        else:
            fm = LoginForm()
        return render(request,'blog/login.html', {'form':fm})
    else:
        return HttpResponseRedirect('Dashboard')
        

def user_signup(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm = SignupForm(request.POST)
            if fm.is_valid():
                messages.success(request,'Congratulations ....! You Become an Author')
                user = fm.save()
                group = Group.objects.get(name='Author')
                user.groups.add(group)
                return HttpResponseRedirect('Dashboard')
        else:
            fm = SignupForm()
        return render(request,'Blog/signup.html',{'form':fm})
    else:
        return HttpResponseRedirect('Dashboard')


def Add_post(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title , desc=desc)
                pst.save()
                form=PostForm()
        else:
            form =PostForm()
        return render(request,'Blog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('Login')


def Update_post(request , id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance = pi)
            messages.success(request,'Updated Successfully....!!!')
        return render(request,'Blog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('Login')


def Delete_post(request ,id ):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('Dashboard')
    else:
        return HttpResponseRedirect('Login')





def detail_contact(request):
    if request.method=='POST':
        people = request.POST
        print(people.get('first_name'))
        
        first_name=people.get('first_name')
        last_name=people.get('last_name')
        email=people.get('email')
        address1=people.get('address1')
        address2=people.get('address2')        
        city=people.get('city')    
        state=people.get('state')
        pincode =people.get('pincode')
        print(first_name)
        contact = ContactModel(first_name=first_name,last_name=last_name,email=email,address1=address1,address2=address2,city=city,state=state,pincode=pincode)
        contact.save()
        return HttpResponseRedirect('thanks')


def thanks(request):
    return render(request,'Blog/thanku.html')

