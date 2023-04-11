from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict

from .forms import * 
from .models import *
from user.models import User
from book_recommendation.common import GetCustomResponse, get_data_or_404


# Create your views here.
@require_http_methods(["POST"])
def add_book_to_shoppingcart(request):
    form = ShoppingCartItemForm(request.POST)
    if not form.is_valid():
        errors = ['Invalid form data']
        return GetCustomResponse(result=False, err_msg=errors, status=400)

    shopping_cart_item = form.save()
    return GetCustomResponse(data=model_to_dict(shopping_cart_item), status=200)


@require_http_methods(["POST"])
def remove_book_from_shoppingcart(request):
    user = request.POST.get('user')
    book = request.POST.get('book')
    sc_item, resp = get_data_or_404(
        ShoppingCartItem, 
        'book', 
        user=user,
        book=book)
    if sc_item is None:
        return resp

    sc_item.delete()
    return GetCustomResponse(status=200)


@require_http_methods(["GET"])
def get_books_in_shoppingcart(request):
    user_id = request.GET.get('user_id')
    req_user, resp = get_data_or_404(User, 'user', id=user_id)
    if req_user is None:
        return resp

    b_items = req_user.shoppingcart.all()
    books = list()
    for b_item in b_items:
        books.append(
            {
                'book_id': b_item.book.id, 
                'book_name': b_item.book.name
            }
        )

    return GetCustomResponse(data=books, status=200)