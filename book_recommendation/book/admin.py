from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "desc",]
    list_per_page = 10
    list_filter = ["name"]
    search_fields = ["name"]

admin.site.register(Book, BookAdmin)