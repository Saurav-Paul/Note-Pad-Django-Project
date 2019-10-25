from django.db import models

# Create your models here.

class Note(models.Model):
    title   = models.CharField(max_length=150)
    desc    = models.TextField()
    date    = models.DateTimeField(auto_now=True)
    owner   = models.CharField(max_length=150,blank = True)