from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
  name = models.CharField(max_length=20)

  class Meta:
    verbose_name_plural = "categories"
  

  def __str__(self):
    return self.name


class Post(models.Model):
  title = models.CharField(max_length=20)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  body = models.TextField()
  venue_image = models.ImageField(null=True, blank=True, upload_to='images/')
  created_on = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  categories = models.ManyToManyField("Category", related_name="blogs")

  def __str__(self):
    return self.title


class Comment(models.Model):
  author = models.CharField(max_length=20)
  body = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name='comments')
  
  def __str__(self):
    return f"{self.author} on '{self.post}'"
