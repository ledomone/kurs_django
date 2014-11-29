from django.contrib import admin

from .models import Author, Publisher, Book, Category, BookItem, BookEdition


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name']
    ordering = ['first_name']


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']


class PublisherAdmin(admin.ModelAdmin):
    search_fields = ['name', 'url']
    ordering = ['name']
    list_display = ['name', 'url']

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Category)
admin.site.register(BookItem)
admin.site.register(BookEdition)