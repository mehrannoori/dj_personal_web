from django.db import models
from django.urls import reverse

class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField(max_length=150)

    class Meta:
        permissions = [
            ('list_message_permit', 'can see messages list'),
        ]

    def __str__(self):
        return self.name + " | " + self.email + " | " + self.message[:40]
    
    def get_absolute_url(self):
        return reverse('home')