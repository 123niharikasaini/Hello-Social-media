from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
# importing User model
from django.contrib.auth.models import User
# for authentication
from django.contrib import auth
# for messages (sending message to frontend==>>like error or success)
from django.contrib import messages
# importing models
from .models import Profile
# decorator
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    # signin the user
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['pass']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('helloHome')
        else:
            messages.info(request,'Credentials invalid')
            return redirect("/")

    else:
        return render(request,'index.html')

def signUp(request):
    # creating user
    if request.method=="POST":
        username=request.POST['userName']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if pass1==pass2:
            # check all objects in User table and then filter on the basis of the email
            if User.objects.filter(email=email).exists():
                # if already exists
                messages.info(request,'Email taken')
                return redirect("signUp")
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect("signUp")
            else:
                # creating the user
                user=User.objects.create_user(username=username,email=email,password=pass1)
                user.save()
                # log user in and redirect to settings page
                user_login=auth.authenticate(username=username,password=pass1)
                auth.login(request,user_login)

                # create a profile object for new user
                user_model=User.objects.get(username=username)
                new_profile=Profile.objects.create(user=user_model,id_user=user_model.id)
                new_profile.save()
                return redirect("settings")
        else:
            messages.info(request,"Password not matching")
            return redirect('signUp')
        # print(username)
    else:
        return render(request,'signUp.html')

def forgetPassword(request):
    return render(request,'forgetPassword.html')

# to prevent unauthorized access
@login_required(login_url="/")
def helloHome(request):
    user_obj=User.objects.get(username=request.user.username)
    user_profile=Profile.objects.get(user=user_obj)
    return render(request,"hello-home.html",{'usder_profile':user_profile})

@login_required(login_url="/")
def signOut(request):
    auth.logout(request)
    return redirect("/")

@login_required(login_url="/")
def settings(request):

    # fetching the data of the user from the profile model 
    user_profile=Profile.objects.get(user=request.user)

    if request.method=="POST":
        
        if request.FILES.get('image')==None:
            image=user_profile.profileImg
            bio=request.POST.get('bio')
            location=request.POST.get('location')

            user_profile.profileImg=image
            user_profile.bio=bio
            user_profile.location=location

            user_profile.save()

        if request.FILES.get('image') != None:
            image=request.FILES.get("image")
            bio=request.POST.get('bio')
            location=request.POST.get('location')

            user_profile.profileImg=image
            user_profile.bio=bio
            user_profile.location=location
            user_profile.save()

        return redirect('settings')

    
    return render(request,'settings.html',{'user_profile':user_profile})

@login_required(login_url="/")
def upload(request):
    return HttpResponse("<h1>Upload Your Views</h1>")