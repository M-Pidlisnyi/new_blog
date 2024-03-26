from django.contrib.auth.models import User
from django.db import models

from django.utils import timezone
# Create your models here.


class BlogUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='pics/', verbose_name="Profile Picture", null=True)
    class Meta:
        verbose_name = "Blog User"
        verbose_name_plural = "Blog Users"



class Category(models.Model):
    name = models.CharField(max_length=25, unique=True, null=False, blank=False)

    class Meta:
        verbose_name_plural = "Categories"

def upload_image_path(instance, filename):
    #images will be loaded to MEDIA_ROOT/<post_id>/filename
    return f"pics/{instance.id}/{filename}"
class Post(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    text = models.TextField()
    datetime = models.DateTimeField(null=False, blank=False, default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="pics/", null=True, blank=True)