from django.contrib import admin

from .models import Team, Technician, Detour, Request


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'name',
        'service',
    ]

@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'name',
        'telephone',
        'team'
    ]

@admin.register(Detour)
class DetourAdmin(admin.ModelAdmin):
    list_display = [
        'get_devation',
        'date',
        'installations',
        'justification',
        'get_technical',
    ]


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'protocol',
        'type',
        'local',
        'status',
        'note',
        'r_factor',
        'team',
    ]
