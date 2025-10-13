from django.contrib import admin
from core import models


class AuthorAdmin(admin.ModelAdmin):
    ordering = ['author_id']
    list_display = [field.name for field in models.Author._meta.fields]


class BookAdmin(admin.ModelAdmin):
    ordering = ['book_id']
    list_display = [field.name for field in models.Book._meta.fields]

class UserAdmin(admin.ModelAdmin):
    ordering = ['user_id']
    list_display = [field.name for field in models.User._meta.fields]


admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.User, UserAdmin)
