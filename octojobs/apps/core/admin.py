from django.contrib import admin

from .models import Wilaya, Commune

@admin.register(Wilaya)
class WilayaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','active']
    list_display_links =('id', 'name')
    list_filter = ['active']
    list_per_page = 30







@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):
    list_display = ('name','wilaya_id')



