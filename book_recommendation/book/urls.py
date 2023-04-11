from django.urls import path
from .views import *


urlpatterns = [
    path('list/', BookListView.as_view(), name='get_book_list'),
    path('detail/', get_book_detail, name='get_book_detail'),
    path('search/', search_book, name='search'),
    path('search_related_book/', search_related_book, name='search_related_book'),
    path('mark/', mark, name='mark'),
    path('random/', get_random_book, name='get_random_book'),
]
