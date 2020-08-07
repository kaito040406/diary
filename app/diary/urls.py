from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num>', views.searchIndex, name='searchIndex'),
    path('show/<int:num>', views.show, name='show'),
    path('create', views.create, name='create'),
    path('form', views.diaryForm, name='diaryForm'),
    path('show/commentform/<int:num>', views.commentForm, name='commentForm'),
    path('search', views.searchForm, name='search'),
]

urlpatterns += staticfiles_urlpatterns()