from django.db import models

# Create your models here.

# create a model for the database of user with the following fields
# id, name, email, password, created_at, updated_at, handle, role, dob


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    handle = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    dob = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
