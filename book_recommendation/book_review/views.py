from django.shortcuts import get_object_or_404
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from datetime import datetime

from .models import BookReview
from book.models import Book
from user.models import User
from .forms import *
from book_recommendation.common import GetCustomResponse, get_data_or_404


# Create your views here.
@require_http_methods(["POST"])
def create_review(request):
    form = CreateBookReviewForm(request.POST)
    if not form.is_valid():
        errors = ['Invalid form data']
        return GetCustomResponse(err_msg=errors, status=400)

    review = form.save()
    return GetCustomResponse(data=model_to_dict(review), status=200)


@require_http_methods(["POST"])
def update_review(request):
    revew_id = request.POST.get('review_id')
    review, resp = get_data_or_404(BookReview, 'review', id=revew_id)
    if review is None:
        return resp

    user_id = request.POST.get('user_id')
    req_user, resp = get_data_or_404(User, 'user', id=user_id)
    if req_user is None:
        return resp

    if req_user != review.user:
        errors = ['Not allow to edit the review not created by yourself']
        return GetCustomResponse(err_msg=errors, status=403)

    form = UpdateBookReviewForm(request.POST, instance=review)
    if not form.is_valid():
        errors = ['Invalid form data']
        return GetCustomResponse(err_msg=errors, status=400)

    update_review = form.save()
    return GetCustomResponse(data=model_to_dict(update_review), status=200)

@require_http_methods(["POST"])
def delete_review(request):
    revew_id = request.POST.get('review_id')
    review, resp = get_data_or_404(BookReview, 'review', id=revew_id)
    if review is None:
        return resp

    user_id = request.POST.get('user_id')
    req_user, resp= get_data_or_404(User, 'user', id=user_id)
    if req_user is None:
        return resp

    if req_user.is_superuser or req_user == review.user:
        review.delete()
        return GetCustomResponse(status=200)
    else:
        errors = ["Not allow to delete the review not created by yourself"]
        return GetCustomResponse(err_msg=errors, status=400)


@require_http_methods(["GET"])
def get_review_list_by_user(request):
    user_id = request.GET.get('user_id')
    user, resp = get_data_or_404(User, 'user', id=user_id)
    if user is None:
        return resp

    review_list = list(user.review.all().values())
    return GetCustomResponse(data=review_list, status=200)

@require_http_methods(["GET"])
def get_review_list_by_book(request):
    book_id = request.GET.get('book_id')
    book, resp = get_data_or_404(Book, 'query book', id=book_id)
    if book is None:
        return resp

    review_list = list(book.review.all().values())
    return GetCustomResponse(data=review_list, status=200)

@require_http_methods(["POST"])
def mark(request):
    review_id = request.POST.get('review_id')
    review, resp = get_data_or_404(BookReview, 'review', id=review_id)
    if review is None:
        return resp

    useful = request.POST.get('useful', None)
    if mark is None:
        errors = ['Invalid request, the value (1 or 0) of useful not found']
        return GetCustomResponse(result=False, err_msg=errors, status=400)
    else:
        useful = int(useful)

    if useful:
        review.N_useful = review.N_useful + 1
    else:
        review.N_not_useful = review.N_not_useful + 1

    review.save()
    return GetCustomResponse(data=model_to_dict(review), status=200)