# coding=utf-8
from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.db import models

from website.models import Movie, Star, Gender, Country

class MovieAdmin(admin.ModelAdmin):
    list_display = ('admin_photo', 'title', 'created_at', 'status')
    list_filter = ('status', 'created_at')
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {models.TextField: {'widget': CKEditorWidget}}
    filter_horizontal = ['gender', 'stars']
    search_fields = ('title',)
    fieldsets = [
        ('Informações principais', {'fields': ['status', 'title', 'slug','synopsis', 'photo', 'trailer', 'gender', 'stars']}),
    ]


class StarAdmin(admin.ModelAdmin):
    list_display = ('admin_photo', 'name', 'created_at', 'country')
    list_filter = ('created_at', )
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name',)
    fieldsets = [
        ('Informações principais', {'fields': ['name', 'slug','country', 'photo']}),
    ]


class GenderAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_filter = ('created_at', )
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name',)
    fieldsets = [
        ('Informações principais', {'fields': ['name', 'slug']}),
    ]

admin.site.register(Movie, MovieAdmin)
admin.site.register(Star, StarAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Country)
