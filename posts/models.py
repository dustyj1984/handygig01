from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model



class Status(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE
        

    )


    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        default=2
    )
   
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    name = models.CharField(max_length=80, blank=True, null=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'



# Create your models here.
