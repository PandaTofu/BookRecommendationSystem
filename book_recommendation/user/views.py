from django.http.response import HttpResponse, JsonResponse
from django.views.generic import CreateView, FormView, DetailView
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.forms.models import model_to_dict

from .models import User
from .forms import UserSignupForm, UserProfileGetForm, UserProfileUpdateForm
from book_recommendation.common import GetCustomResponse, get_data_or_404


def get_errors(form):
    errors = form.errors.get_json_data()
    error_list = []
    for key, value in errors.items():
        for error_info in value:
            error_list.append(error_info['message'])
    return error_list


@require_http_methods(["POST"])
def signup(request):
    form = UserSignupForm(request.POST)
    if form.is_valid():
        form.save()
        return GetCustomResponse(status=201)
    else:
        errors = get_errors(form)
        return GetCustomResponse(result=False, err_msg=errors, status=400)


@require_http_methods(["POST"])
@sensitive_post_parameters()
@never_cache
def login(request):
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        auth_login(request, user)
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
        data = {'user_id': user.id}
        return GetCustomResponse(data=data, status=200)
    else:
        errors = get_errors(form)
        return GetCustomResponse(result=False, err_msg=errors, status=401)


def logout(request):
    auth_logout(request)
    body = {
            "resule": True,
            "err_msg": [],
            "data": {}
    }
    return HttpResponse("Logged out", status=200)


@require_http_methods(["GET"])
def user_profile(request):
    user_id = request.GET.get('user_id', None)
    user, resp = get_data_or_404(User, 'user', id=user_id)
    if user is None:
        return resp

    profile = {
        'username': user.username,
        'email': user.email,
        'gender': user.gender
    }
    return GetCustomResponse(data=profile, status=200)


@sensitive_post_parameters()
@require_http_methods(["POST"])
def password_change(request):
    user_id = request.POST.get('user_id')
    user, resp = get_data_or_404(User, 'user', id=user_id)
    if user is None:
        return resp

    form = PasswordChangeForm(user=user, data=request.POST)
    if form.is_valid():
        form.save()
        return GetCustomResponse(status=200)
    else:
        errors = ["Invalid request"]
        return GetCustomResponse(err_msg=errors, status=400)

@require_http_methods(["POST"])
def update_profile(request):
    form = UserProfileUpdateForm(request.POST)
    user_id = form.data['user_id']
    user, resp = get_data_or_404(User, 'user', id=user_id)
    if user is None:
        return resp

    if form.is_valid():
        data = form.data
        user.email = data.get('email', user.email)
        user.gender = data.get('gender', user.gender)
        user.save()
        profile = {
            'username': user.username,
            'email': user.email,
            'gender': user.gender
        }
        return GetCustomResponse(data=profile, status=200)
    else:
        errors = ["Invalid request"]
        return GetCustomResponse(err_msg=errors, status=400)

@require_http_methods(["GET"])
def search(request):
    username = request.GET.get('username')
    user, resp = get_data_or_404(User, 'user', username=username)
    if user is None:
        return resp

    data = model_to_dict(user)
    return GetCustomResponse(result=True, data=data, status=200)

