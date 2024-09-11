from django.contrib import admin

from .models import Book, Review


class ReviewInline(admin.TabularInline):
    model = Review


class BookAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]


admin.site.register(Book, BookAdmin)
