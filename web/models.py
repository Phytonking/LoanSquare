from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Message(models.Model):
    name = models.TextField()
    email = models.EmailField()
    date_sent = models.DateTimeField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.date_sent}"
