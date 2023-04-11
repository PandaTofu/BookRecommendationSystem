from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>/create/', PreferenceBookCreateView.as_view(), name='add_preference'),
    path('list/', PreferenceBookListView.as_view(), name='preference_list'),
]
