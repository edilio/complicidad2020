from django.contrib import admin

from . import models


@admin.register(models.Poem)
class PoemAdmin(admin.ModelAdmin):
    list_filter = ('draft', 'updated_at')
    list_display = ('title', 'draft', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_per_page = 25


@admin.register(models.Frase)
class FraseAdmin(admin.ModelAdmin):
    list_filter = ('draft', 'updated_at')
    list_display = ('draft', 'author', 'created_at', 'updated_at')
    search_fields = ('content',)
    list_per_page = 25
