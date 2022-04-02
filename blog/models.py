from django.db import models
from django.contrib.auth.models import User


class UserExtension(models.Model):
    avatar= models.ImageField(upload_to="avatar",blank=True, null=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    link= models.URLField(null=True)
    more_description= models.CharField(max_length=100)
