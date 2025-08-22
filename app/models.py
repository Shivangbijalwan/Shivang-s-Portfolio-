from django.db import connection, models
from django.shortcuts import render
from urllib3 import request

class Contact(models.Model):
    name = models.CharField(max_length=100) 
    subject = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    comment = models.TextField()


    def __str__(self):
        return self.name
    


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()   # ✅ This must exist
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


