from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topics(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    topics = models.ForeignKey(Topics, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    desc = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created", "-updated"]

    def __str__(self) -> str:
        return self.name


class Mensage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.body[0:30]
    
    class Meta:
        ordering = ["-created", "-updated"]