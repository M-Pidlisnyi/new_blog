from django.shortcuts import render
from .models import Category

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")


def category(request, category_id):
    current_category = Category.objects.get(id=category_id)
    return render(request, "category.html", context={"category": current_category})