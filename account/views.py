from django.shortcuts import render,redirect
from . models import User
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib import auth
# Create your views here.

class Login(TemplateView):
    template_name = 'account/signin.html'


def signup(request):
    if request.method == 'POST':

        data = request.POST
        username = data.get('username','')
        password = data.get('password','')
        confirm_password = data.get('cpassword')
        email = data.get('email','')
        phone_number = data.get('phone_number','')
        first_name = data.get('fname','')
        last_name = data.get('lname')
        profile = data.get('profile')


        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            user.set_password(password)
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.success(request, 'Profile updated successfully!')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match. Please try again.')
            return render(request, 'account/signup.html')

        if 'image' in request.FILES:
            profile = request.FILES['image']
            data = User.objects.create_user(username=username,password = password,email=email,phone_number=phone_number,first_name=first_name,last_name=last_name,profile=profile)
            data.save()
            messages.success(request, 'Account created successfully!')
            return render(request, 'account/signup.html')

    return render(request, 'account/signup.html')  # Redirect to profile page after update


def Signin(request):
    if request.method =='POST':
        data = request.POST
        username = data.get('username','')
        password = data.get('password','')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully signed in!')
            return redirect('home')  # Redirect to a home page or dashboard
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return render(request, 'account/signin.html', {'data': data})

    return render(request,'account/signin.html')



def logout(request):
    auth.logout(request)
    return redirect('login')