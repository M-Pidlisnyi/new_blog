from django.contrib import admin
from .models import BlogUser, Category, Post
# Register your models here.
admin.site.register(BlogUser)
admin.site.register(Category)
admin.site.register(Post)