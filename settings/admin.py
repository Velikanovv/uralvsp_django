from django.contrib import admin

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.
from .models import SocialMediaSetting, MenuSetting, FooterContacts, SecondBlockAbouts, BlocksSettings, PSSettings, MenuUrl, Politics, Contacts, MessageSettings, Page


admin.site.register(SocialMediaSetting)
admin.site.register(MenuSetting)
admin.site.register(FooterContacts)
admin.site.register(SecondBlockAbouts)
admin.site.register(BlocksSettings)
admin.site.register(PSSettings)
admin.site.register(MenuUrl)
admin.site.register(MessageSettings)




class PoliticsAdminForm(forms.ModelForm):
    text = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())
    class Meta:
        model = Politics
        fields = '__all__'

@admin.register(Politics)
class PoliticsAdmin(admin.ModelAdmin):
    form = PoliticsAdminForm


class ContactsAdminForm(forms.ModelForm):
    text = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())
    class Meta:
        model = Contacts
        fields = '__all__'

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    form = ContactsAdminForm


class PageAdminForm(forms.ModelForm):
    text = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())
    class Meta:
        model = Page
        fields = '__all__'

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm