from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('show/<int:num>', views.show, name='show'),
    path('create', views.create, name='create'),
    path('form', views.form, name='form'),
    path('show/commentform/<int:num>', views.commentForm, name='commentForm'),
]

urlpatterns += staticfiles_urlpatterns()