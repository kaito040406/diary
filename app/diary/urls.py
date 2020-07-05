from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('dataid/show', views.show, name='show'),
    path('create', views.create, name='create'),
    path('form', views.form, name='form'),
]

urlpatterns += staticfiles_urlpatterns()