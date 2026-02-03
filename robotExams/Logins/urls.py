from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='Logins/login.html'), name='login'),
    path('exams/', views.exams, name='exams'),
]
