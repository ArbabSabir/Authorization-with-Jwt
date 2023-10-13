from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User


# class CustomUser(AbstractBaseUser):
#     email = models.EmailField(unique=True)  # Use email as the unique identifier

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

