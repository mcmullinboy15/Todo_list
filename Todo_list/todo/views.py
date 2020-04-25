import itertools
from pprint import pprint
import json
from requests.compat import urljoin, quote_plus


import requests
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils import timezone
from django.core import serializers
from django.contrib.auth.models import User, UserManager, AbstractUser
from django.forms.models import model_to_dict

from .models import Project, List, Task


def convert(request):
    _from = request.GET.get('from')
    _to = request.GET.get('to')
    value = request.GET.get('value')
    print(_from, _to, value)

    resp = None
    if 'value' not in request.GET:
        resp = {'error': 'Invalid unit conversion request'}
    else:
        n = request.GET['value']
        try:
            n = float(n)

            # change = Change.objects.filter(_from=_from, _to=_to)[0]
            send__ = None  # float(value) * float(change.value)
            # print(send__)

            resp = {
                "units": _to,
                "value": send__
            }

        except:
            resp = {'error': 'Invalid unit conversion request'}

    response = JsonResponse(resp)
    response['Access-Control-Allow-Origin'] = '*'
    return response


# Create your views here.
def index(request):
    return render(request, 'todo/index.html', {'time': timezone.now()})


def user_index(request, user_id):
    # user = User.objects.filter(pk=user_id)[0]
    
    # print(request.build_absolute_uri(f"/todo/{user_id}/api/project/"))
    # # print(urljoin(request, f"/todo/{user_id}/api/project/"))
    # # response = requests.get(f"http://3.19.7.49:8080/todo/{user_id}/api/project/")
    # response = requests.get(request.build_absolute_uri(f"/todo/{user_id}/api/project/"))
    #
    # user_data = response.json()
    #
    # user = user_data['User']
    # todos = user_data['Projects']

    return render(request, 'todo/user_index.html', {'time': timezone.now(), 'user_id': user_id, })


def get_projects(user_id, proj_id, amount):
    projs = Project.objects.filter(pk=proj_id)  # TODO I'll need to add user filtering (_user=user_id)
    projs = list(projs)

    if amount is 'all':
        print('amount is all')
        return projs

    # get the Project with pk = { the passed value }
    for pro_ in projs:
        if pro_.pk != proj_id:
            projs.exclude(pk=pro_.pk)

    return projs[:amount]


def get(request, user_id):
    """
    Arguments:
        project: int
        list: int
        task: int
    """
    dict = {}
    proj_id = request.GET.get('project')
    list_id = request.GET.get('list')
    task_id = request.GET.get('task')
    amount = request.GET.get('amount')

    print(proj_id)
    print(list_id)
    print(task_id)

    has_proj_id = False
    has_list_id = False
    has_tasks_id = False
    has_amount = False

    if amount is None:
        amount = 'all'
    else:
        amount = int(amount)

    if proj_id is not None:
        has_proj_id = True

        projects = get_projects(user_id, proj_id, amount)

        projects_json = serializers.serialize('json', projects)

        dict.update({'projects': projects_json})

        pprint(dict)

    if list_id is None:

        if task_id is None:
            has_list_id = True

    if task_id is not None:

        has_tasks_id = True

        # get all it's lists
        lists = List.objects.filter(_project=proj_id)

        for list in lists:
            # call the get method again to get the lists
            lists_json = requests.get(f"http://127.0.0.1:8000/{user_id}/get?list={list.pk}")

            # print(lists_json)
            dict.update(lists_json)

    # TODO later i will make it do another request for the Lists and Tasks but for now I'm just going to use proj_id to
    #  get everything

    # lists = serializers.serialize("json", lists)
    # dict.update({'lists':lists})
    # print(lists)
    #
    # # get all the list's tasks
    # lists = List.objects.filter(_project=proj_id)
    # lists = serializers.serialize("json", lists)
    # dict.update({'lists':lists})
    # print(lists)
    #
    #
    # print(dict)

    # if list_id.isnumeric():
    #     # get the List with pk = { thie passed value }
    #     lists = List.objects.filter(pk=list_id)  # I'll need to add user filtering
    #     lists = serializers.serialize("json", lists)
    #     dict.update({'list': lists})
    #     print(lists)
    #
    #     # create proj from an array of the one possible Project
    #     list = lists[0]
    #     print(list)
    #
    # elif list_id == 'all':
    #
    #     lists = List.objects.filter(_project=proj_id)
    #
    #
    #     dict.update({f'list{list_id}':list})

    # add a header {'type': type}  type would be Project, List, Task

    response = JsonResponse(dict, safe=False)
    response['Access-Control-Allow-Origin'] = '*'

    return response


def new(request, user_id):
    return JsonResponse({'time': timezone.now()})


def link(request, user_id):
    link = request.GET.get('link')  # boolean is False do an unlink
    return JsonResponse({'time': timezone.now()})


def delete(request, user_id):
    return JsonResponse({'time': timezone.now()})


def reassign(request, user_id):
    return JsonResponse({'time': timezone.now()})


def add(request, user_id):
    return JsonResponse({'time': timezone.now()})
