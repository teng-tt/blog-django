'''
    自定义模板标签
'''
from django import template
from .. models import Post,Category

#实例化template.Library类
register = template.Library()

#使用装饰器装饰，最新文章模板标签，返回5篇文章
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

#文章归档模板标签
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

#分类模板标签
@register.simple_tag
def get_categories():
    return Category.objects.all()