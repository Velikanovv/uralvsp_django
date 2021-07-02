from django.contrib import admin
# Register your models here.
from .models import News

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class NewsAdminForm(forms.ModelForm):
    text = forms.CharField(label='Текст поста', widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        fields = '__all__'

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_filter = ('date',)
    readonly_fields = ('date',)
    form = NewsAdminForm