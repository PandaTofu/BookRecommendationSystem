from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("login/", login, name='login'),
    path("logout/", logout, name='logout'),
    path("signup/", signup, name='signup'),
    path("profile/", user_profile, name='profile'),
    path("password_change/", password_change, name='password_change'),
    path("update_profile/", update_profile, name='update_profile'),
    path("search/", search, name="search"),
]