from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

# User = get_user_model()
class Project(models.Model):
    project_title = models.CharField(max_length=200)
    stack = models.CharField(max_length=200)
    message = models.TextField()
    check_code = models.URLField(max_length=300)
    live_page = models.URLField(max_length=300)

    
    def __str__(self):
        return self.project_title
    

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username
    
# class Category(models.Model):
#     title = models.CharField(max_length=30)
#     subtitle = models.CharField(max_length=20)
    # slug = models.SlugField() 
    # thumbnail = models.ImageField()

    # def __str__(self):
    #     return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    # title_tag = models.CharField(max_length=100)
    # slug = models.SlugField()
    # overview = models.TextField()
    time_posted = models.DateField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # thumbnail = models.ImageField()
    snippet = models.CharField(max_length=200, default= 'Read More') 

    # categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
    

    