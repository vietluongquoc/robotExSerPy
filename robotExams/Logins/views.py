from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import UserProfile

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('exams')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login.html')

@login_required
def exams(request):
    if request.method == "POST":
        print(request.POST)  # Prints the POSTed data as a QueryDict
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Here you would typically validate the username and password
        # For demonstration, we will just print them
        print(f"Username: {username}, Password: {password}")
    return render(request, "exams.html")