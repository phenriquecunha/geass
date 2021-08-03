from django.contrib import admin

from .models import Team, DailyMonitoring, TypeOfRequest, Technician, Detour, Request

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

@admin.register(DailyMonitoring)
class DailyMonitoringAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'current_balance',
        'open',
        'completed',
        'previous_balance',
        'type_of_request'
    ]

@admin.register(TypeOfRequest)
class TypeOfRequestAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'name',
        'weight',
    ]

@admin.register(Detour)
class DetourAdmin(admin.ModelAdmin):
    list_display = [
        'date',
        'installations',
        'detour',
        'justification',
        'get_technical',
    ]


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'protocol',
        'local',
        'status',
        'note',
        'r_factor',
        'type_of_request',
        'team',
    ]
