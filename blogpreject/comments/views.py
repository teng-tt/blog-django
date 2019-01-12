from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from . models import Comment
from . froms import CommentForm

def post_comment(request,post_pk):
    #获取被评论的文章
    post = get_object_or_404(Post,pk=post_pk)
    #判断用户请求为提交时才处理数据
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {'post':post,'form':form,'coment_list':comment_list}
            return render(request,'blog/detail.html',context=context)
    return redirect(post)


