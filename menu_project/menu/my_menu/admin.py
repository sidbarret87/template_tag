from django.contrib import admin
from .models import *

class GenreAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
admin.site.register(Genre, GenreAdmin)

class BooksAdmin(admin.ModelAdmin):
    list_display = ('title','genre','author')
    search_fields = ('title','genre')
admin.site.register(Books, BooksAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','genre')
    list_display_links = ('name','genre')
    search_fields = ('name','genre')
admin.site.register(Author, AuthorAdmin)
# Register your models here.
