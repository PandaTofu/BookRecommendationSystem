from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.http.response import JsonResponse
from django.core import serializers
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict
from django.db.models import Q
import difflib
from functools import reduce
import operator
from decimal import Decimal
import random


from .models import Book
from book_recommendation.common import GetCustomResponse, get_data_or_404
from .forms import MarkForm

# Create your views here.
class BookListView(ListView):
	model = Book
	template_name = 'book_list.html'
	
	#Uncomment the below codes to get json body instead of html.
	def get(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		data = {'data': list(queryset.values())}
		return JsonResponse(data, status=200, safe=False)

	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

    #Uncomment the below codes to get json body instead of html.
    def get(self, request, *args, **kwargs):
    	book = model_to_dict(self.get_object())
    	book['cover'] = str(book['cover'])
    	data = {'data': book}
    	return JsonResponse(data, status=200, safe=False)

    def dispatch(self, request, *args, **kwargs):
    	return super().dispatch(request, *args, **kwargs)

@require_http_methods(["GET"])
def get_book_detail(request):
    book_id = request.GET.get('book_id')
    book, resp = get_data_or_404(Book, 'book', id=book_id)
    if book is None:
        return resp

    data = model_to_dict(book)
    data['cover'] = str(data['cover'])
    return GetCustomResponse(data=data, status=200)

@require_http_methods(["GET"])
def search_book(request):
    condition = request.GET.dict()
    name_kw = condition.pop('name')

    book_list = Book.objects.filter(**condition).\
                             filter(name__icontains=name_kw).\
                             order_by('-mark').values()
    return GetCustomResponse(data=list(book_list), status=200)

@require_http_methods(["GET"])
def search_related_book(request):
    book_id = request.GET.get('book_id')
    book, resp = get_data_or_404(Book, 'book', id=book_id)
    if book is None:
        return resp

    name = book.name
    condition = {
        'author': book.author,
        'genre': book.genre,
    }
    print(name)
    book_list = Book.objects.filter(**condition).\
                             filter(name__icontains=name).\
                             order_by('-mark').values()

    books = Book.objects.filter(**condition).exclude(name=name)
    if len(books) == 0:
    	return GetCustomResponse(status=200)

    book_names = [obj['name'] for obj in list(books.values('name'))]
    similar_names = difflib.get_close_matches(name, book_names)

    if len(similar_names) == 0:
    	return GetCustomResponse(status=200)
    
    query = reduce(operator.or_, (Q(name=x) for x in similar_names))
    book_list = Book.objects.filter(query).values()
    return GetCustomResponse(data=list(book_list), status=200)

@require_http_methods(["POST"])
def mark(request):
    book_id = request.POST.get('book_id')
    book, resp = get_data_or_404(Book, 'book', id=book_id)
    if book is None:
        return resp

    form = MarkForm(request.POST)
    if not form.is_valid():
    	errors = ['Invalid mark, the value should be [0.0, 10.0]']
    	return GetCustomResponse(result=False, err_msg=errors, status=400)

    req_mark = Decimal(request.POST.get('mark'))
    n_mark = book.N_mark
    new_mark = (book.mark * n_mark + req_mark) / (n_mark + 1)
    book.mark = round(new_mark, 1)
    book.N_mark = n_mark + 1
    book.save()
    data = model_to_dict(book)
    data['cover'] = str(data['cover'])
    return GetCustomResponse(data=data, status=200)


@require_http_methods(["GET"])
def get_random_book(request):
    book_list = Book.objects.all().values()
    if len(book_list) == 0:
        errors = ['No book in the system']
        return GetCustomResponse(result=False, err_msg=errors, status=404)

    n_book = len(book_list)
    random_id = random.randint(0, n_book-1)
    book = book_list[random_id]
    return GetCustomResponse(data=book, status=200)

