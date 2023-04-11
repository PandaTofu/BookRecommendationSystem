from django.shortcuts import get_object_or_404
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict
from django.views.generic import ListView, CreateView
from django.core import serializers

from book.models import Book
from .models import PreferenceBook


# Create your views here.
class PreferenceBookCreateView(CreateView):
    model = PreferenceBook
    template_name = 'preference_book_add.html'

    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, id=kwargs.get('pk', None))
        return self.render_to_response(self.get_context_data(book=book))

    def get_context_data(self, **kwargs):
        context = {}
        context['book'] = kwargs.get('book', None)
        return context

    def post(self, request, *args, **kwargs):
        book = get_object_or_404(Book, id=kwargs.get('pk', None))
        preference = PreferenceBook(book=book, user=request.user)
        preference.save()
        return JsonResponse(model_to_dict(preference), status=201)


class PreferenceBookListView(ListView):
    model = PreferenceBook
    template_name = 'book_review_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = serializers.serialize("json", queryset)
        return JsonResponse(data, status=200, safe=False)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
