from django.contrib import admin
from .models import IncidentDown

# Register your models here.
class IncidentDownAdmin(admin.ModelAdmin):
    list_display = (
        'caller_id', 
        'emailAdress', 
        'description', 
        'comments', 
        'impact', 
        'urgency', 
        'worknotes', 
        'assignment_group',
        'state', 
        'date', 
        'is_process'
        )
    
admin.site.register(IncidentDown, IncidentDownAdmin)