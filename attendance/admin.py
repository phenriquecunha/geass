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
         '__str__',
         'city',
         'district',
         'street',
         'latitude',
         'longitude',
         'service',
         'user',
    ]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'name',
        'answer',
        'user',
    ]

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'name',
        'client',
        'questions',
        'note',
        'user',
    ]

@admin.register(Service)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'nameFlat',
        'infrastructure',
        'user',
    ]