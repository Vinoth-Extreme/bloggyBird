from django.contrib import admin
from .models import Post, Category, Profile, Comments

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Comments)
