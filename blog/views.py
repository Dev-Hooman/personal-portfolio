from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.db.models import Count
from django.contrib import messages


from blog.models import Blog , BlogComment
import string


def blog(request):

    allPost = Blog.objects.all()

    context = {
        'allPost':allPost,
    }

    return render(request, 'blog/blog.html',context)



def blogPost(request, slug):
    blogPost = Blog.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=blogPost)

    context = {
        'blogPost' : blogPost,
        'comments' : comments,
    }
    return render(request, 'blog/blogPost.html', context)


def postComment(request):

    if request.method=="POST":
        comment = request.POST.get("comment")
        user = request.user
        
        postSno = request.POST.get("postSno")
        post = Blog.objects.get(sno=postSno)

        comment = BlogComment(comment=comment, user=user, post=post)
        comment.save()
      
        messages.success(request, 'Your Comment has been posted sucessfully!')
        

    return redirect(f"/blog/{post.slug}")

