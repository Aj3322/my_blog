from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class AuthorUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    bio = models.TextField(blank=True)  
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True) 
    email = models.EmailField() 
    last_login = models.DateTimeField(null=True, blank=True) 
    last_password_change = models.DateTimeField(null=True, blank=True) 
    last_profile_update = models.DateTimeField(null=True, blank=True)  
    followers = models.ManyToManyField(User, related_name='following', blank=True)  
    following = models.ManyToManyField(User, related_name='followers', blank=True) 

    def __str__(self):
        return self.user.username
    class Meta:
          db_table = 'authorusers'
     


class Blog(models.Model):
  Blog_id = models.CharField(max_length=255)
  Blog_title = models.CharField(max_length=255)
  def __str__(self):
        return self.Blog_id
  class Meta:
        db_table = 'blog_Table'
        
        
class Blog2(models.Model):
  Blog_id = models.CharField(max_length=255)
  Blog_title = models.CharField(max_length=255)
  def __str__(self):
        return self.Blog_id
  class Meta:
        db_table = 'blog_Table2'

