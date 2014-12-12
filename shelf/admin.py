from django.contrib import admin

from .models import Author, Publisher, Book, BookCategory, BookItem, BookEdition


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


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', ]


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(BookCategory)
admin.site.register(BookItem)
admin.site.register(BookEdition)