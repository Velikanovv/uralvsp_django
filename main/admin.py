from django.contrib import admin


from .models import FeedBack, Application

@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['text', 'date']
    list_filter = ['date']



@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone','date']
    list_filter = ['date']
    search_fields = ['name', 'email', 'phone','date']