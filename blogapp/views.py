from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Category, Post, BlogUser

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    blog_user = BlogUser.objects.get_or_create(user=request.user)[0]


    if request.method == "POST":
        print(request.FILES)
        profile_pic = request.FILES.get('profile_pic', None)
        print(profile_pic)
        blog_user.profile_pic = profile_pic
        blog_user.save()
        return  HttpResponseRedirect(reverse('about'))
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


def view_post(request, post_id):
    current_post = Post.objects.get(id=post_id)
    return  render(request, "post.html", context={"post": current_post})

def search_results(request):
    if not request.method == "POST":
        response = HttpResponse()
        response.reason_phrase = "Method not allowed"
        response.status_code = 405
        return response
    else:
        search_term = request.POST.get("search_term")
        posts_list = Post.objects.filter(title__icontains=search_term)
        #TODO add Postgresql DB using docker to make icontains work
        return render(request, "search_results.html", context={"posts": posts_list})
