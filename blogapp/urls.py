from django.urls import path, include

from blogapp import views

urlpatterns = [
    path('', views.index, name='index')
]