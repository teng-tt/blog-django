import markdown
from django.shortcuts import render,get_object_or_404
from . models import Post,Category
from comments.froms import CommentForm

# Create your views here.

#index视图图函数
def index(request):
    post_list = Post.objects.all()
    return render(request,'blog/index.html',context={'post_list':post_list})

#文章详情页视图
def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.body = markdown.markdown(post.body,
            extensions=[
                         'markdown.extensions.extra',
                         'markdown.extensions.codehilite',
                         'markdown.extensions.toc',
                       ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    context ={'post':post,'form':form,'comment_list':comment_list}
    return render(request,'blog/detail.html',context=context)

#文章归档视图函数,根据年月过滤
def archives(request,year,month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month)
                                    
    return render(request,'blog/index.html',context={'post_list':post_list})

#分类视图函数
def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request,'blog/index.html',context={'post_list':post_list})