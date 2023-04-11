from django.urls import path
from .views import *


urlpatterns = [
    path('create/', create_wishlist, name='create_wishlist'),
    path('delete/', delete_wishlist, name='delete_wishlist'),
    path('add_book/', add_book_to_wishlist, name='add_book'),
    path('remove_book/', remove_book_from_wishlist, name='remove_book'),
    path('get_wishlist/', get_wishlist, name='get_wishlist'),
    path('get_books/', get_books_in_wishlist, name='get_books'),
]
