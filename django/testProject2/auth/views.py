from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required




# Create your views here.
def register(request):

    # handle registration process
    if request.method == "POST":
        data = request.POST

        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        # check if username exists
        try:
            user = User.objects.filter(username=username).first()
            if user:
                messages.error(request, "Username already exists"),
                return render(
                    request,
                    "auth/register.html",
                    {"error": "Username already exists"},
                )
        except Exception as e:
            messages.error(request, "An error occurred on username check"),
            return render(
                request,
                "auth/register.html",
                {"error": "An error occurred on username check"},
            )

        # check if email exists
        try:
            user = User.objects.filter(email=email).first()
            if user:
                messages.error(request, "Email already exists")
                return render(
                    request,
                    "auth/register.html",
                    {"error": "Email already exists"},
                )
        except Exception as e:
            messages.error(request, "An error occurred on email check")
            return render(
                request,
                "auth/register.html",
            )

        # create user

        try:
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()
            print("User created == ", user)
            return redirect("register")
        except Exception as e:
            messages.error(request, "An error occurred on user creation"),
            return render(
                request,
                "auth/register.html",
                {"error": "An error occurred on user creation"},
            )

    return render(request, "auth/register.html")


# log in views
def login_view(request):
    # handle login proceess

    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")

        print("username == ", username)
        print("password == ", password)

        try:
            u = User.objects.filter(username=username).exists()
            if not u:
                messages.error(request, "Invalid username")
                return render(request, "auth/login.html")
        except Exception as e:
            messages.error(request, "An error occurred on username check")
            return render(request, "auth/login.html")

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid password")
            return render(request, "auth/login.html")
        else:
            login(request, user)
            return redirect("home")

    return render(request, "auth/login.html")


# log out views
def logout_view(request):
    logout(request)
    return redirect("login")
