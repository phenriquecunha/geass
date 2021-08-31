from django.contrib import admin

from .models import Register

@admin.register(Register)
class TeamAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'date',
        'protocol',
        'type_of_request',
        'sent_to',
        'clerk'
    ]