from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager
from django.db.models.fields.files import ImageField
from django.forms.fields import DateTimeField

# Create your models here.
class User_Post(models.Model):
    main_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name="main_user")
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    shared_users=models.ManyToManyField(User, related_name="shared_users")