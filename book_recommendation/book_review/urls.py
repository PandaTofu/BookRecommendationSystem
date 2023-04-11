from django.urls import path
from .views import *


urlpatterns = [
    path('create/', create_review, name='create_review'),
    path('update/', update_review, name='update_review'),
    path('delete/', delete_review, name='delete_review'),
    path('list/by_book/', get_review_list_by_book, name='get_review_list_by_book'),
    path('list/by_user/', get_review_list_by_user, name='get_review_list_by_user'),
    path('mark/', mark, name='mark'),
]
