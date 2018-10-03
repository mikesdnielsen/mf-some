from django.contrib import admin

from .models import Like, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'created_at']
    list_select_related = ('author', )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['post', 'user']
    list_select_related = ('post', 'user')
