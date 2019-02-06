from django.db import models
from django.contrib.auth.models import User

# Character model used to store information on user's characters.
class Character(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User)