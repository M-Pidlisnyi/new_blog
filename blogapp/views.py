from django.shortcuts import render
from .models import Category, Post, BlogUser


# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    blog_user = BlogUser.objects.get(user=request.user)
    return render(request, "about.html", context={"blog_user": blog_user})


def category(request, category_id):
    current_category = Category.objects.get(id=category_id)
    posts_list = Post.objects.filter(category=category_id)

    return render(request, "category.html", context={"category": current_category, "posts": posts_list})