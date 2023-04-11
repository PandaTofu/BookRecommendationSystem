from django.urls import path
from .views import *


urlpatterns = [
    path('add_book/', add_book_to_shoppingcart, name='add_book'),
    path('remove_book/', remove_book_from_shoppingcart, name='remove_book'),
    path('get_books/', get_books_in_shoppingcart, name='get_books'),
]