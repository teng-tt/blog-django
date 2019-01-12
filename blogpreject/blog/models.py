'''
    定义数据模型（数据库表）
'''
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#定义文章分类表
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

#定义文章标签表
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

#定义文章数据表
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField()
    moodified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200,blank=True)
    #数据表关联分类表，由于一边文章只能有一个分类，一个分类可以有多篇文章为一对多关系
    #所以使用ForeignKey类型

    category = models.ForeignKey(Category)
    #数据表关联标签表，由于一个标签可以有多篇文章，一篇文章可以有多个标签为多对多的关系
    #所以使用ManyToManyFiled类型  
     
    tag = models.ManyToManyField(Tag,blank=True)
    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
    author = models.ForeignKey(User) 

    def __str__(self):
        return self.title

    #自定义get_absolute_url方法
    #    
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})
    
    #定义文章排序子类
    class Meta:
        ordering = ['-created_time']
