from django.contrib import admin

from .models import AdvUser

class AdvUserAdmin(admin.ModelAdmin):
    '''
        Admin View for AdvUser
    '''
    list_display = ('username', 'first_name', 'last_name', 'is_activated',)

admin.site.register(AdvUser, AdvUserAdmin)
