from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import ProductModel, ProductCategoryModel


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = ProductModel
        fields = "__all__"


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price',)
    search_fields = ('name',)
    list_filter = ('category',)
    empty_value_display = '-пусто-'
    form = ProductAdminForm


@admin.register(ProductCategoryModel)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('slug',)
    empty_value_display = '-пусто-'