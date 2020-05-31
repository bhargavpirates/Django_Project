from django.db import models

# Create your models here.

class BlogComment(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.CharField(max_length=10000)