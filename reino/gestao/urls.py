from django.urls import path

from gestao import views

urlpatterns = [
    path('', views.index, name='index'),
]