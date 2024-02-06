from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
