from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body = models.TextField()
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)

    class Meta:
        permissions = [
            ('special_status', 'can edit post')
        ]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})