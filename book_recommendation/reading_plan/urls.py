from django.urls import path
from .views import *


urlpatterns = [
    path('create/', create_plan, name='create_plan'),
    path('delete/', delete_plan, name='delete_plan'),
    path('list/', get_plan_list, name='plan_list'),
    path('clock/', clock_plan, name='clock'),
]
