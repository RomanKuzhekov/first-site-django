from django.contrib import admin
from .models import *

admin.autodiscover ()

admin.AdminSite.site_header = 'Админка сайта - Строительство домов в Волгограде'

admin.site.register(Category)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'id', 'category', 'created_date', 'bit',)
    search_fields = ['title']
    list_filter = ['category']
admin.site.register(Post, PostAdmin)


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'approwed_article', 'created_date', 'bit',)
    search_fields = ['title']
    list_filter = ['created_date']
admin.site.register(Articles, ArticlesAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author','text', 'approwed_comment', 'created_date',)
    search_fields = ['text']
    list_filter = ['created_date']
admin.site.register(Comment, CommentAdmin)

class PhotosAdmin(admin.ModelAdmin):
    list_display = ('bit', 'Photo', 'Slider_Up', 'Slider_Down', 'created_date',)
    list_filter = ['created_date']
admin.site.register(Photos, PhotosAdmin)

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('author','phone', 'created_date',)
    search_fields = ['author']
    list_filter = ['created_date']
admin.site.register(Orders, OrdersAdmin)