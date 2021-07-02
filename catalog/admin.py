from django.contrib import admin

# Register your models here.
from .models import Production, Service, Category, SubCategory, Product, SubProduct, ProductParam, ProductValue


from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ProductAdminForm(forms.ModelForm):
    text = forms.CharField(label='Текст продукта', widget=CKEditorUploadingWidget())
    class Meta:
        model = Product
        fields = '__all__'

class SubCategoryAdminForm(forms.ModelForm):
    text = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())
    class Meta:
        model = SubCategory
        fields = '__all__'

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    list_filter = ['category']
    form = SubCategoryAdminForm

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'subcategory']
    list_filter = ['subcategory']
    form = ProductAdminForm

@admin.register(SubProduct)
class SubProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'product']
    list_filter = ['product']

@admin.register(ProductParam)
class ProductParamAdmin(admin.ModelAdmin):
    list_display = ['title', 'product']
    list_filter = ['product']

admin.site.register(Production)
admin.site.register(Service)
admin.site.register(Category)