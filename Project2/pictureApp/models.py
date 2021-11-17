from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.files import ImageField
from django.forms.fields import DateField, DateTimeField

# Create your models here.
class User_Post(models.Model):
    main_user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    date = models.DateField(auto_now_add=False)