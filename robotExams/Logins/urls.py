from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', auth_views.LoginView.as_view(template_name='Logins/login.html'), name='login'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('exams', views.exams, name='exams'),
    path('results', views.results, name='results'),
]
