from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager
from django.db.models.fields.files import ImageField
from django.forms.fields import DateTimeField
import os

# Create your models here.
class User_Post(models.Model):
    main_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name="main_user")
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    shared_users=models.ManyToManyField(User, related_name="shared_users", null=True, default=None)
    
    def __str__(self):
        return os.path.basename(self.image.name)
    
    
class User_Albums(models.Model):
    album_name = models.CharField(unique=True, max_length=120)
    albumDescription = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name="creator")
    contents = models.ManyToManyField(User_Post,related_name="contents",default=None)
    
    def __str__(self):
        return str(self.album_name)