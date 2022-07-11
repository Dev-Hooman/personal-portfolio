from turtle import title
from django.shortcuts import render

#-------Models Import for Database-------
from home.models import contact
from blog.models import Blog
#----------------------------------------

#-----------Alert Message-----------
from django.contrib import messages
#-----------------------------------

#-----------Email Send Module-----------
from django.core.mail import send_mail
from django.conf import settings
#---------------------------------------

def home(request):

    allPost =  Blog.objects.filter().order_by('-pub_date')[0:2]
    print(allPost)
    context = {
        'allPost':allPost,
    }

    return render(request, 'home/index.html',context)

def about(request):
    
    return render(request, 'home/about.html')


def projects(request):
    
    return render(request, 'home/projects.html')


def contactUs(request):
    message_Display = None
    if request.method == "POST":
        senderName = request.POST['name']
        senderPhone = request.POST['phone']
        senderEmail = request.POST['email']
        senderContent = request.POST['content']

        if len(senderName) <2 or len(senderEmail)<3 or len(senderContent)<10 or len(senderPhone)<10:
            messages.error(request, "Please be carefull while filling the form")
            message_Display = "Ohh Darn!"
        else:

            send_mail(
                f'Message From {senderName} To user',
                f'\t {senderContent} \n \n {senderName} details : \n Phone: {senderPhone} \n Email: {senderEmail} ',
                settings.EMAIL_HOST_USER,
                ['octupuspc@gmail.com'],
                fail_silently=False,
            )

            Contact = contact(name=senderName, phone=senderPhone, email=senderEmail, content=senderContent)
            Contact.save()

            message_Display = "Yahooo!!"
            messages.success(request, 'Your Message has been successfully sent!')

    context = {'messageDisplay' : message_Display,}
    
    return render(request, 'home/contact.html', context)

def search(request):
    message_Display = None

    query = request.GET['query']

    #query size
    if len(query) > 70:
        searchPost = Blog.objects.none()
    else:
        searchTitle = Blog.objects.filter(title__icontains = query)
        searchContent = Blog.objects.filter(content__icontains = query)

        searchPost = searchTitle.union(searchContent)

    if searchPost.count() == 0:
        message_Display = "Warning:"
        messages.warning(request, 'No search resut found, please try again!')
        #query = "";
        
         
    context = {
        'searchPost' : searchPost,
        'query' : query,
        'messageDisplay' : message_Display,
    
     }
    
    return render(request, 'home/search.html', context)