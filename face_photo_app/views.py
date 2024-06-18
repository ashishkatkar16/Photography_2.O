from django.shortcuts import render


# ------------------------ ADMIN VIEWS ------------------------
def admin_home(request):
    return render(request, "Admin/home.html")


def admin_index(request):
    return render(request, "Admin/__index.html")


def admin_signup(request):
    return render(request, "Admin/signup.html")


def admin_dashboard(request):
    return render(request, "Admin/dashboard.html")


# ------------------------ ADMIN END ------------------------

# ------------------------ USER VIEWS ------------------------

def user_dashboard(request):
    return render(request, "User/dashboard.html")


def user_index(request):
    return render(request, "User/__index.html")


def user_otp(request):
    return render(request, "User/otp.html")


def user_selfie(request):
    return render(request, "User/selfie.html")

# ------------------------ USER END  ------------------------
