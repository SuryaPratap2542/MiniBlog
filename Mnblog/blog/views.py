from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,SetPasswordForm,PasswordChangeForm
from .forms import SignUpForm,LoginForm,PostForm,ContactForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from .models import Post,Contact
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

# Create your views here.

#home
def home(request):
    posts=Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})

#about
def about(request):
    return render(request,'blog/about.html')

def miniblog(request):
    return render(request,'blog/miniblog.html')

def miniblog1(request):
    return render(request,'blog/miniblog1.html')

#Contact
def contact(request):
    return render(request,'blog/contact.html')

#Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        user=request.user
        full_name=user.get_full_name()
        gps=user.groups.all()
        return render(request,'blog/dashboard.html',{'posts':posts,'full_name':full_name,'groups':gps})
    else:
        return HttpResponseRedirect('/login/')

#Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

#Sign_up
def user_signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, "Congratulation!! You have become an Author")
            user=form.save()
            group=Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        form =SignUpForm()
    # return render(request,'blog/signup.html',{'form':form})
    return render(request,'blog/customerregistration.html',{'form':form})

#Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                usname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user = authenticate(username=usname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Login successfully !!")
                    return HttpResponseRedirect('/dashboard/')
        else:
            form=LoginForm()
        return render(request,'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')
    


# Add new post
def add_post(request):
    if  request.user.is_authenticated:
        if request.method=="POST":
            form = PostForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title, desc=desc)
                pst.save()
                form = PostForm()
                messages.success(request, 'Post added successfully.')  # Add success message

        else:
            form=PostForm()
        return render(request, 'blog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('login')
    
# Update  post
def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                messages.success(request, 'Post Updated successfully.')  # Add success message
                return HttpResponseRedirect('/dashboard/')  # Replace '/success/' with the desired URL

        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        
        return render(request, 'blog/updatepost.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/') 
    
# Delete post
def delete_post(request,id):
    if  request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('login')
    
def user_contact(request):
    if  request.user.is_authenticated:
        if request.method=="POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                name=form.cleaned_data['name']
                email = form.cleaned_data['email']
                message=form.cleaned_data['message']
                cont = Contact(name=name, email=email,message=message)
                cont.save()
                form = ContactForm()
                messages.success(request, 'Message sent successfully.')  # Add success message
        else:
        
            form=ContactForm()
        return render(request, 'blog/user_contact.html',{'form':form})
    else:
        return HttpResponseRedirect('login')
