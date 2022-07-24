from django.contrib import admin

from blog.models import Blog, BlogComment

admin.site.register(BlogComment)



@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)

