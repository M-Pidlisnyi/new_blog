from django.contrib.auth.models import User
from django.db import models
from django.db.models import OneToOneField
from django.utils import timezone
# Create your models here.


class BlogUser(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='pics/', verbose_name="Profile Picture", null=True)
    class Meta:
        verbose_name = "Blog User"
        verbose_name_plural = "Blog Users"



class Category(models.Model):
    name = models.CharField(max_length=25, unique=True, null=False, blank=False)

    class Meta:
        verbose_name_plural = "Categories"

class Post(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    text = models.TextField()
    datetime = models.DateField(null=False, blank=False, default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)