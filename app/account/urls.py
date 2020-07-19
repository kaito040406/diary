from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('registrationResult', views.registrationResult, name='registrationResult'),
]

urlpatterns += staticfiles_urlpatterns()