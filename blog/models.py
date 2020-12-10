from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse # return full path as a string

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
        

#  >>> for post in posts_json:
# ...     post=Post(title=post['title'], content=post['content'], author_id=post['user_id'])