from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from blog.templatetags import extras
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
    comments = BlogComment.objects.filter(post=blogPost ,parent=None)
    replies = BlogComment.objects.filter(post=blogPost ).exclude(parent=None)
    
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
            
    commentsCount = BlogComment.objects.count()

    context = {
        'blogPost' : blogPost,
        'comments' : comments,
        'commentsCount' : commentsCount,
        'user' : request.user,
        'replyDict': replyDict,
    }
    return render(request, 'blog/blogPost.html', context, )


def postComment(request):

    if request.method=="POST":
        comment = request.POST.get("comment")
        user = request.user
        
        postSno = request.POST.get("postSno")
        post = Blog.objects.get(sno=postSno)

        parentSno = request.POST.get("parentSno")

        if parentSno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
        
            messages.success(request, 'Your Comment has been posted sucessfully!')
        else:
            parents = BlogComment.objects.get(sno=parentSno) 
            comment = BlogComment(comment=comment, user=user, post=post , parent=parents)
            comment.save()
            messages.success(request, 'Your Reply has been posted sucessfully!')

    return redirect(f"/blog/{post.slug}")

