from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=250)
    title_tag = models.CharField(max_length=250,)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    post_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title +' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse("home")
    
