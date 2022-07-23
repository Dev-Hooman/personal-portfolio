from django.contrib import admin

<<<<<<< HEAD
from blog.models import Blog, BlogComment

admin.site.register(BlogComment)



@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)
=======
# from blog.models import Blog, BlogComment
from blog.models import Blog

admin.site.register(Blog)
# admin.site.register(BlogComment)
>>>>>>> 804c4325be9c245b0fb53a81731dad7632e4bcd5
