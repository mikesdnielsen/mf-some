from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import FriendRelationship

User = get_user_model()


class FriendInline(admin.StackedInline):
    model = FriendRelationship
    fk_name = 'from_user'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'full_name', 'date_joined']
    search_fields = ['email', 'full_name', 'short_name']

    inlines = [FriendInline]
