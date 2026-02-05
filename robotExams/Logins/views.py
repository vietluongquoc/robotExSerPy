from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        print(f"Attempting login for user: {username}, password: {password}")
        
        if user is not None:
            login(request, user)
            return redirect('exams')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def exams(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        

    return render(request, "exams.html")