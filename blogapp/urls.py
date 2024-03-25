from django.urls import path, include

from blogapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post')
]