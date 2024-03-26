from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
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

    if request.method == "POST":
        print(request.FILES)
        new_title = request.POST.get("title")
        new_text = request.POST.get("text", "")
        new_image = request.FILES.get("image", None)
        print(new_image)
        blog_user = BlogUser.objects.get(user=request.user)
        Post.objects.create(title=new_title, text=new_text, category=current_category, user=blog_user, image=new_image)
        return  HttpResponseRedirect(reverse("category", args=(current_category.id,)))


    return render(request, "category.html", context={"category": current_category, "posts": posts_list})

def delete_post(request, post_id):
    deleted_post = Post.objects.get(id=post_id)
    deleted_post.delete()
    return HttpResponseRedirect(reverse("category", args=(deleted_post.category_id,)))