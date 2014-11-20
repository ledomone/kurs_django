from django.contrib import admin

from .models import Author, Publisher, Book


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name']
    ordering = ['first_name']


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'author', 'isbn', 'publisher']


class PublisherAdmin(admin.ModelAdmin):
    search_fields = ['name', 'url']
    ordering = ['name']
    list_display = ['name', 'url']

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
