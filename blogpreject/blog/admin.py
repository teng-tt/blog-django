from django.contrib import admin
from .models import Post,Category,Tag
# Register your models here.

#定制admin后台
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_time','moodified_time','category','author']

#注册自定义的模型（数据表）把上面定制的也注册进来
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
