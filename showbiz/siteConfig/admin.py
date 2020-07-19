from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.



class ContactAdmin(admin.ModelAdmin):
    '''Admin View for Contact'''

    list_display = (
        'nom',
        'email',
        'website',
        'status',
        'date_add',
        'date_update'
    )
    list_filter = (
        'status',
        'date_add',
        'date_update',
    )
    search_fields = (
        'nom',
        'email',
    )
    list_per_pages = 50
    date_hierarchy = 'date_add'
  

    fieldsets = [
        ('Info ', {'fields': ['titre','nom','email','website','message',]}),
        ('Status et Activations', {'fields': ['status', ]}),
    ]




class BreakingAdmin(admin.ModelAdmin):
    '''Admin View for Contact'''

    list_display = (
        'heure',
        'annonce',
        'status',
        'date_add',
        'date_update'
    )
    list_filter = (
        'status',
        'date_add',
        'date_update',
    )
    search_fields = (
        'date_add'
    )
    list_per_pages = 50
    date_hierarchy = 'date_add'
  

    fieldsets = [
        ('Info ', {'fields': ['titre','heure','annonce',]}),
        ('Status et Activations', {'fields': ['status', ]}),
    ]


def _register(model,admin_class):
    admin.site.register(model,admin_class)

_register(models.Contact,ContactAdmin)
_register(models.Breaking,BreakingAdmin)