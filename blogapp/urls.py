from django.urls import path, include

from blogapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<int:category_id>/', views.category, name='category')
]