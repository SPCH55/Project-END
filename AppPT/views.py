# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm

def home(request):
    return render(request, 'home.html')

# แสดงรายละเอียดการจองของสนาม
def booking_detail(request):

    return render(request, 'booking_detail.html')

def booking(request):
    return render(request, 'booking.html')

# Register view
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():  # ตรวจสอบว่าฟอร์มถูกต้องหรือไม่
            form.save()  # บันทึกข้อมูลลงในฐานข้อมูล
            messages.success(request, "Registration successful.")
            return redirect('login')  # เปลี่ยนไปยังหน้า login
    else:
        form = RegisterForm()  # สร้างฟอร์มเปล่าในกรณี GET request
    return render(request, 'register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # เปลี่ยนเส้นทางไปหน้า home
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}! You are now logged in.")
                return redirect('home')  # เปลี่ยนเส้นทางไปที่หน้า home
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

