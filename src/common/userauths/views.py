from django.shortcuts import render, redirect
from common.userauths.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from common.userauths.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import re

# Checks if the password is valid.
def password_check(password):
    """ Takes one argument (str) password. Returns true if password contains at least 8 characteres with upper case, 
    lower case, alpha-numeric, and special characters"""

    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"\W", password) is None
    password_ok = not (
        length_error or digit_error or uppercase_error or lowercase_error or symbol_error)

    if password_ok:
        return True
    else:
        return False

# Using this method you have control over the messages and creating the contexts.
def register(request):

    if request.method == "POST":
        email = request.POST.get("email").strip()
        username = request.POST.get("username").strip().lower().replace(" ", "")
        full_name = request.POST.get("full_name").strip()
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        email_exists = User.objects.filter(email=email).exists()
        username_exists = User.objects.filter(username=username).exists()

        context = {
            "usrename": username,
            "email": email,
            "full_name": full_name,
        }

        if len(email) < 5 or len(email) > 254:
            messages.error(request, "Email must be valid")
            context["email"] = ""
            return render(request, 'userauths/register.html', context)
        
        elif email_exists:
            messages.error(request, "Email is already taken")
            context["email"] = ""
            return render(request, 'userauths/register.html', context)

        elif len(username) < 4:
            messages.error(request, "Username must be at least 4 characters")
            context["username"] = ""
            return render(request, 'userauths/register.html', context)
        
        elif username_exists:
            messages.error(request, "Username is already taken")
            context["username"] = ""
            return render(request, 'userauths/register.html', context)
                        
        elif password1!= password2:
            messages.error(request, "Passwords do not match")
            return render(request, 'userauths/register.html', context)

        elif not password_check(password1):
            messages.error(request, "Password must contain at least 8 characters with upper case, lower case, alpha-numeric, and special characters")
            return render(request, 'userauths/register.html', context)

        else:   
            
            User.objects.create_user(username=username, email=email, full_name=full_name, password=password1)
            return HttpResponse("Account created successfully")

    return render(request, 'userauths/register.html',)


# There are two ways to do this. If you use the built in form then you do not have control over the messages and creating the contexts.

def login_page(request):

    if request.method == "POST":
        email = request.POST.get("email").strip()
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:home')
        else:
            messages.error(request, "Invalid username or password")

        

    return render(request, 'userauths/login.html')


def logout_page(request):
    logout(request)
    return redirect('userauths:login')


def check_username_availability(request):
    username = request.GET.get("username")
    username = username.strip().lower()
    available = not User.objects.filter(username=username).exists()

    if len(username) < 4 or " " in username:
        return JsonResponse({"success": False}, status=200)
    if available:
        return JsonResponse({"success": True}, status=200)
    else:
        return JsonResponse({"success": False}, status=200)
    

def register_using_form(request):

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        email = request.POST.get("email")
        username = request.POST.get("username")
        full_name = request.POST.get("full_name")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if form.is_valid():
            user = form.save(commit=False)
            user.email = email
            user.username = username
            user.full_name = full_name
            user.set_password(password1)
            print(form.cleaned_data['email']) # works
            # user.save()
            return HttpResponse("Account created successfully")
        
        if form.errors:
            for key, value in form.errors.items():
                messages.error(request, value.as_text().replace("*", ""))
                break
            return render(request, 'userauths/register.html')

    return render(request, 'userauths/register.html',)

