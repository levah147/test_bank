from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def dashboard(request):
    return render(request, 'core/dashboard.html')

def register(request):
    return render(request, 'auth/auth-register.html')

def login(request):
    return render(request, 'auth/auth-login.html')

def reset_password(request):
    return render(request, 'auth/auth-reset-password.html')

def forgot_password(request):
    return render(request, 'auth/auth-forgot-password.html')