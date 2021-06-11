from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Article(models.Model):

    
    title = models.CharField(max_length = 150, verbose_name='عنوان')
    slug = models.SlugField(max_length= 150, unique = True , verbose_name='ادرس لینک')
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='article', verbose_name='نویسنده')
    content = models.TextField(verbose_name='توضیحات')
    publish = models.DateTimeField(default = timezone.now,verbose_name='منتشر شده')
    created = models.DateTimeField(auto_now_add=True,verbose_name='ساخته شده')
    updated = models.DateTimeField(auto_now=True,verbose_name='بروز رسانی شده')
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title