from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registration', views.registration, name='registration'),
    # path('login', views.login, name='login'),
    # path('login', django.contrib.auth.views.LoginView, {'template_name': 'accounts/login.html'}, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('registrationResult', views.registrationResult, name='registrationResult'),
    path('loginResult', views.loginResult, name='loginResult'),
]

urlpatterns += staticfiles_urlpatterns()