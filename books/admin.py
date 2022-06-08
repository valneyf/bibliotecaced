from django.contrib import admin

from .models import Author, Category, Book


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'modified']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'category',
        'author',
        'published',
        'pages',
        'is_available',
        'created',
        'modified',
    ]
    list_filter = ['is_available', 'created', 'modified']
    list_editable = ['category', 'author',
                     'published', 'pages', 'is_available']
