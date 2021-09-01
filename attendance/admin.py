from django.contrib import admin

from .models import Register, Client, Question, Quiz, Service

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'date',
        'protocol',
        'type_of_request',
        'sent_to',
        'clerk'
    ]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
         
    ]