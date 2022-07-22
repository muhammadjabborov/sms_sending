from django.contrib import admin

from app.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass