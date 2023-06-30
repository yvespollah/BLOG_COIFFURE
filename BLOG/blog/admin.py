from django.contrib import admin
from .models import *

# Register your models here.
#on va les enregistrer sur forme de table cest pour sa que on va cree une class
class BlogAdmin(admin.ModelAdmin):
    list_display=('titre','intro','slug','date_added')

class CommentAdmin(admin.ModelAdmin):
    list_display=('body','email','date_added')


admin.site.register(CreateBlog,BlogAdmin)
admin.site.register(Comment,CommentAdmin)


