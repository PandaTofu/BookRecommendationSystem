from django.shortcuts import get_object_or_404
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict
from django.views.generic import ListView, CreateView
from django.core import serializers
from datetime import date, timedelta

from .models import ReadingPlan
from book.models import Book
from user.models import User
from .forms import ReadingPlanForm
from book_recommendation.common import GetCustomResponse, get_data_or_404


# Create your views here.
@require_http_methods(["POST"])
def create_plan(request):
    form = ReadingPlanForm(request.POST)
    if not form.is_valid():
        errors = ['Invalid form data']
        return GetCustomResponse(result=False, err_msg=errors, status=400)

    plan = form.save()
    return GetCustomResponse(data=model_to_dict(plan), status=200)

@require_http_methods(["GET"])
def get_plan_list(request):
    user_id = request.GET.get('user_id')
    req_user, resp = get_data_or_404(User, 'user', id=user_id)
    if req_user is None:
        return resp

    plan_list = req_user.plan.all().values()
    return GetCustomResponse(data=list(plan_list), status=200)

@require_http_methods(["POST"])
def delete_plan(request):
    plan_id = request.POST.get('plan_id')
    plan, resp = get_data_or_404(ReadingPlan, 'plan', id=plan_id)
    if plan is None:
        return resp

    plan.delete()
    return GetCustomResponse(status=200)


@require_http_methods(["POST"])
def clock_plan(request):
    plan_id = request.POST.get('plan_id')
    plan, resp = get_data_or_404(ReadingPlan, 'plan', id=plan_id)
    if plan is None:
        return resp

    if plan.is_completed:
        errors = ['This plan is already completed']
        return GetCustomResponse(result=False, err_msg=errors, status=400)

    if plan.last_clock_date == date.today():
        errors = ['already clock']
        return GetCustomResponse(result=False, err_msg=errors, status=400)

    plan.clock_days = plan.clock_days + 1
    plan.last_clock_date = date.today()
    if plan.clock_days == plan.period_days:
        plan.is_completed = True
    plan.save()

    return GetCustomResponse(data=model_to_dict(plan), status=200)

