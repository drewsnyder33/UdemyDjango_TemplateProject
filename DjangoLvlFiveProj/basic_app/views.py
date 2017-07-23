from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm

# import stuff for login functionality
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in.")

@login_required # decorator to require that the user be logged in in order to execute this view
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save() # save general user data from UserForm into database
            user.set_password(user.password) # hashes user's password
            user.save() # re-saves user data into database, basically updating it for hashed password

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'basic_app/registration.html',
                 {'registered':registered,
                 'user_form':user_form,
                 'profile_form':profile_form})

# Make sure not to name view function "login", since this name was already imported above and would confuse Django
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # next line uses built in django method to automatically authenticate
        # username & password in just one line
        user = authenticate(username=username, password=password)

        if user:  # if user was successfully authenticated in line above
            if user.is_active:
                login(request,user) # function imported above to handle login in 1 line
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not active. Please reactivate your account.")

        else:
            print("Someone tried to login and failed!")
            print("Username: {} and Password: {}".format(username, password))
            return HttpResponse("Invalid login details; please try again.")
    else:
        return render(request, 'basic_app/login.html',{})
