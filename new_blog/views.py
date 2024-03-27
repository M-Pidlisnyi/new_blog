from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login
from django.urls import reverse

def signup(request):
    alert = None
    if request.method == 'POST':
        email = request.POST.get("email", None)
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        if password == password_confirm:
            user = User.objects.create_user(
                email=email,
                username=username,
                password=password
            )
            login(request, user)
            return HttpResponseRedirect(reverse("about"))

        else:
            alert = "Passwords don't match"



    return render(request, "registration/signup.html", context={"alert": alert})