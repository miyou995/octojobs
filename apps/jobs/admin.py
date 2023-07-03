from django.contrib import admin
from .models import  Tag, Job, Application


class ApplicationInline(admin.TabularInline):
    model = Application
    extra = 1




@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'is_active',)
    list_display_links = ('id','name' )


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id','title','type','category', 'status', 'budget', 'duration',  'deadline', 'is_active', 'expiration', 'location')

    list_display_links = ('id', 'title' )
    inlines = [ApplicationInline]
    list_per_page = 50




@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'job', 'applicant','selected',)
    # list_editable = ('job', 'applicant','selected',)

    # list_display_links = ('id', 'job', 'applicant',)

