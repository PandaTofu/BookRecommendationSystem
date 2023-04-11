from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict

from .models import *
from .forms import *
from book_recommendation.common import GetCustomResponse, get_data_or_404


# Create your views here.
@require_http_methods(["POST"])
def create_wishlist(request):
    form = WishListForm(request.POST)
    if not form.is_valid():
        errors = ['Invalid form data']
        return GetCustomResponse(result=False, err_msg=errors, status=400)

    wish_list = form.save()
    return GetCustomResponse(data=model_to_dict(wish_list), status=200)

@require_http_methods(["POST"])
def delete_wishlist(request):
    wish_list_id = request.POST.get('wish_list_id')
    wish_list, resp = get_data_or_404(WishList, 'whish list', id=wish_list_id)
    if wish_list is None:
        return resp

    wish_list.delete()
    return GetCustomResponse(status=200)

@require_http_methods(["POST"])
def add_book_to_wishlist(request):
    form = RelationshipForm(request.POST)
    if not form.is_valid():
        errors = ['Invalid form data']
        return GetCustomResponse(result=False, err_msg=errors, status=400)

    relationship = form.save()
    return GetCustomResponse(data=model_to_dict(relationship), status=200)

@require_http_methods(["POST"])
def remove_book_from_wishlist(request):
    form = RelationshipForm(request.POST)
    if not form.is_valid():
        errors = ['Invalid form data']
        return GetCustomResponse(result=False, err_msg=errors, status=400)

    relationship = BookWishListRelationship.objects.get(
    	wish_list=form.data['wish_list'],
    	book=form.data['book'])

    relationship.delete()
    return GetCustomResponse(status=200)


@require_http_methods(["GET"])
def get_wishlist(request):
    wish_list_id = request.GET.get('wish_list_id')
    wish_list, resp = get_data_or_404(WishList, 'whish list', id=wish_list_id)
    if wish_list is None:
        return resp

    return GetCustomResponse(data=model_to_dict(wish_list), status=200)

@require_http_methods(["GET"])
def get_books_in_wishlist(request):
    wish_list_id = request.GET.get('wish_list_id')
    wish_list, resp = get_data_or_404(WishList, 'whish list', id=wish_list_id)
    if wish_list is None:
        return resp

    rs_list = wish_list.relationship.all()
    books = list()
    for rs in rs_list:
        books.append(
            {
                'book_id': rs.book.id, 
                'book_name': rs.book.name
            }
        )

    return GetCustomResponse(data=books, status=200)