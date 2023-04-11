from django.contrib import admin
from .models import BookType


# Register your models here.
class BookTypeAdmin(admin.ModelAdmin):
    list_display = ["book_type", ]
    list_per_page = 10
    #list_filter = ["book_name"]
    #search_fields = ["book_name"]

admin.site.register(BookType, BookTypeAdmin)
