import itertools
from pprint import pprint
import json
from time import sleep

from requests.compat import urljoin, quote_plus

import requests
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils import timezone
from django.core import serializers
from django.contrib.auth.models import User, UserManager, AbstractUser
from django.forms.models import model_to_dict
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

from .models import Project, List, Task


# Create your views here.
def index(request):
    return render(request, 'todo/index.html', {'time': timezone.now()})


# @login_required(login_url='/accounts/login/')
def User(request, user_id):

    # username = request.POST['username']
    # password = request.POST['password']
    # user = authenticate(request, username=username, password=password)

    # if user is not None:
    #     login(request, user)
    # else:
    #     return JsonResponse({'invalid': 'login error message'})

    return render(request, 'todo/user_index.html', {'time': timezone.now(), 'user_id': user_id, })


def Project(request, user_id, proj_id):
    return render(request, 'todo/user_index.html', {'time': timezone.now(), 'user_id': user_id, 'proj_id': proj_id, })


def List(request, user_id, proj_id, list_id):
    return render(request, 'todo/user_index.html', {'time': timezone.now(), 'user_id': user_id, 'proj_id': proj_id, 'list_id': list_id, })


def Task(request, user_id, proj_id, list_id, task_id):
    return render(request, 'todo/user_index.html', {'time': timezone.now(), 'user_id': user_id, 'proj_id': proj_id, 'list_id': list_id, 'task_id': task_id, })
