from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import UserProfile

# Create your views here.
def login_view(request):
    return render(request, 'login.html')

@login_required
def exams(request):
    # if request.method == "POST":
    #     print(request.POST)  # Prints the POSTed data as a QueryDict
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     # Here you would typically validate the username and password
    #     # For demonstration, we will just print them
    #     print(f"Username: {username}, Password: {password}")
    return render(request, "exams.html")