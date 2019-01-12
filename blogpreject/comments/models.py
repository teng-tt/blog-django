'''
    定义评论模块数据模型（数据表）
'''
from django.db import models
# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateField(auto_now_add=True)

    #评论关联文章，一对一类型，一个评论只能关联一篇文章
    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:20]
