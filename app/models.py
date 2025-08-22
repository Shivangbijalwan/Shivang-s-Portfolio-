from django.db import models
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
    

    


