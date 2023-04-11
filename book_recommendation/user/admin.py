from django.contrib import admin
from .models import User


# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "avatar", "gender"]
    list_per_page = 10
    list_filter = ["username", "email"]
    search_fields = ["username"]


admin.site.site_header = ' book recommendation systems'
admin.site.site_title = ' book recommendation systems'

admin.site.register(User, UserInfoAdmin)

