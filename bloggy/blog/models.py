from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse_lazy, reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(upload_to='header_images/', null=True, blank=True)
    title_tag = models.CharField(max_length=255)
    category = models.CharField(max_length=100, default='Uncategorized...')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(null=True, blank=True)
    # body = models.TextField(null=True, blank=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    snippet = models.CharField(max_length=50, default='Click the title to read this article in detail...')
    likes = models.ManyToManyField(User, related_name='blog_post')
    loves = models.ManyToManyField(User, related_name='love_post')

    def totalLikes(self):
        return self.likes.count()

    def totalLoves(self):
        return self.loves.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author) + ' | ' + str(self.publication_date)

    def get_absolute_url(self):
        return reverse('home')


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    website_url = models.CharField(max_length=200, null=True, blank=True)
    facebook_url = models.CharField(max_length=200, null=True, blank=True)
    instagram_url = models.CharField(max_length=200, null=True, blank=True)
    twitter_url = models.CharField(max_length=200, null=True, blank=True)
    linkedin_url = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.user) + " | Profile"

    def get_absolute_url(self):
        return reverse('home')

class Comments(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    done_by = models.ForeignKey(User, related_name='done_by', on_delete=models.CASCADE, null=True,blank=True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ' %s - %s ' % (self.post.title, self.done_by)