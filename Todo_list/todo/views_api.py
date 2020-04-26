from pprint import pprint
from django.forms.models import model_to_dict

import requests
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils import timezone
from django.contrib.auth.models import User, UserManager, AbstractUser

from .models import Project, List, Task

from .Error_Responses import error_resp

"""    blog.comment_set.all()    """


def not_found_resp(objs, user_id, proj_id=None, list_id=None, task_id=None, is_task=False):
    options = {}

    if len(objs) <= 0:
        options.update({'EmptyList': 'There is no Objects connected to this Object'})
        return options
    else:

        type_ = objs[0].type

        _id = user_id
        _id = proj_id if type_ is 'Project' else \
            list_id if type_ is 'List' else \
                task_id if type_ is 'Task' else None

        if _id is None:
            return {'not_found_resp()': 'type_ is None', 'objs': model_to_dict(objs[0])}

        error = {'error': f'{type_} with id {{ {_id} }} was not Found'}

        for obj in objs:
            if proj_id is None:
                options.update({obj.id: f'http://127.0.0.1:8000/todo/{user_id}/'})
            elif list_id is None:
                options.update({obj.id: f'http://127.0.0.1:8000/todo/{user_id}/api/project/{obj.id}/'})
            elif task_id is None:
                options.update({obj.id: f'http://127.0.0.1:8000/todo/{user_id}/api/project/{proj_id}/list/{obj.id}'})
            elif is_task:
                options.update(
                    {
                        obj.id: f'http://127.0.0.1:8000/todo/{user_id}/api/project/{proj_id}/list/{list_id}/task/{obj.id}'})

    error.update({'Available_Options': options})
    return error


def manipulate_TODO_objects(request, TYPE, user_id, proj_id=None, list_id=None):
    variables = getVariables(request)
    details = variables['details']

    resp = {}

    print("TYPE", TYPE, "user_id", user_id, "proj_id", proj_id)

    if TYPE.type == Project.type:
        FORGIEN_TYPE = User

    elif TYPE.type == List.type:
        FORGIEN_TYPE = Project

    elif TYPE.type == Task.type:
        FORGIEN_TYPE = List

    else:
        FORGIEN_TYPE = None

    print((variables['no_command']))
    if not bool(variables['no_command']):

        if variables['create']:
            print("Creating an Object")

            obj = TYPE(
                title=details['title'],
                description=details['description'],
                content=details['content'],
                created=timezone.now(),
                contributors=details['contributors'],
                collapsed=details['collapsed'],

            )
            print(FORGIEN_TYPE)

            # try "User"+error_resp['forgienkry_error']
            # TODO I will fix this to just rename all the objects Forgien_Keys to [parent] or something
            if TYPE.type == Project.type:

                try:
                    obj.parent_obj = get_object_or_404(FORGIEN_TYPE, pk=user_id)
                except:

                    error = not_found_resp(FORGIEN_TYPE.objects.all(), user_id)
                    return {'error': error_resp['forgienkey_error'], 'Object_not_found': error}

            elif TYPE.type == List.type:

                try:
                    obj.parent_obj = get_object_or_404(FORGIEN_TYPE, pk=proj_id)
                except:

                    error = not_found_resp(FORGIEN_TYPE.objects.all(), user_id, proj_id)
                    return {'error': error_resp['forgienkey_error'], 'Object_not_found': error}

            elif TYPE.type == Task.type:

                try:
                    obj.parent_obj = get_object_or_404(FORGIEN_TYPE, pk=list_id)  # id=int(details['foreign']))
                except:

                    error = not_found_resp(FORGIEN_TYPE.objects.all(), user_id, proj_id, list_id)
                    return {'error': error_resp['forgienkey_error'], 'Object_not_found': error}

            else:
                return error_resp['error_type']

            obj.save()

            resp = model_to_dict(obj)
            return resp

        elif variables['edit']:

            print(" :: ", details['id'],
                  details['title'],
                  details['description'],
                  details['content'],
                  details['contributors'],
                  details['collapsed'],
                  )

            try:

                obj = get_object_or_404(TYPE, pk=details['id'])
                print(obj)

                obj.title = details['title'] if (details['title'] is not None) else obj.title
                obj.description = details['description'] if (details['description'] is not None) else obj.description
                obj.content = details['content'] if (details['content'] is not None) else obj.content
                obj.contributors = details['contributors'] if (
                        details['contributors'] is not None) else obj.contributors
                obj.collapsed = details['collapsed'] if (details['collapsed'] is not None) else obj.collapsed

                print(obj)

                obj.save()

                return details

            except:

                print('sup')
                error = not_found_resp(FORGIEN_TYPE.objects.all(), user_id)
                return {'error': error_resp['forgienkey_error'], 'Object_not_found': error}

        elif variables['link']:
            return

        elif variables['delete']:

            try:
                obj = get_object_or_404(TYPE, pk=details['id'])
                obj.delete()

                return {'Object Deleted': model_to_dict(obj)}

            except:
                error = not_found_resp(FORGIEN_TYPE.objects.all(), user_id)
                return {'error': error_resp['forgienkey_error'], 'Object_not_found': error}

        elif variables['add_cont']:
            return
        else:
            return error_resp['error_no_command']

    else:
        # Edit this to a try: except: error

        print(TYPE)

        if TYPE.type == Project.type:
            print('Project.type')

            parent = get_object_or_404(FORGIEN_TYPE, pk=user_id)

            resp.update({f'User': model_to_dict(parent)})

            objs = TYPE.objects.filter(parent_obj=parent)

            objs_dict = {}
            for obj in objs:
                objs_dict.update({f'{TYPE.type}_{obj.id}': model_to_dict(obj)})

            resp.update({f'{TYPE.type}s': objs_dict})

        elif TYPE.type == List.type:
            print('List.type')

            parent = get_object_or_404(FORGIEN_TYPE, pk=proj_id)

            resp.update({f'{parent.type}': model_to_dict(parent)})

            objs = TYPE.objects.filter(parent_obj=parent)

            objs_dict = {}
            for obj in objs:
                objs_dict.update({f'{TYPE.type}_{obj.id}': model_to_dict(obj)})

            resp.update({f'{TYPE.type}s': objs_dict})

        elif TYPE.type == Task.type:
            print('Task.type')

            parent = get_object_or_404(FORGIEN_TYPE, pk=list_id)
            print(parent)

            resp.update({f'{parent.type}': model_to_dict(parent)})

            objs = TYPE.objects.filter(parent_obj=parent)
            print(objs)

            objs_dict = {}
            for obj in objs:
                objs_dict.update({f'{TYPE.type}_{obj.id}': model_to_dict(obj)})

            resp.update({f'{TYPE.type}s': objs_dict})

        else:
            return error_resp['error_type']

        return resp


def getVariables(request):
    dict = {}
    create = request.GET.get('create')
    edit = request.GET.get('edit')
    link = request.GET.get('link')  # unlink
    delete = request.GET.get('delete')
    add_cont = request.GET.get('add_cont')

    commands = [create, edit, link, delete, add_cont]

    has_command = False
    for v in commands:
        v = bool(v)
        if v is True:
            has_command = True

    if not has_command:
        pprint(dict)
        print('There is no Command: ', has_command)
        dict.update(
            {'info': 'Due to the fact that there are no commands the Object and it\'s children will be displayed'})
        dict.update({'no_command': True})

        return dict
    else:
        dict.update({'no_command': False})
        dict.update({'create': create, 'edit': edit, 'link': link, 'delete': delete, 'add_cont': add_cont})

    id = request.GET.get('id')
    title = request.GET.get('title')
    description = request.GET.get('description')
    content = request.GET.get('content')
    contributors = request.GET.get('contributors')
    collapsed = request.GET.get('collapsed')

    dict.update(
        {
            'details':
                {
                    'id': id, 'title': title, 'description': description,
                    'content': content, 'contributors': contributors, 'collapsed': collapsed
                }
        }
    )

    pprint(dict)

    return dict


# Create your views here.
def User__(request):
    variables = getVariables(request)

    if variables['no_command']:
        return getEverything(request)
    else:

        username = request.GET.get('username')
        email = request.GET.get('email')
        password = request.GET.get('password')

        usr = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        usr.is_staff = request.GET.get('is_staff')
        usr.is_superuser = request.GET.get('is_superuser')

        usr.save()

        return JsonResponse(model_to_dict(usr))


def project_list(request, user_id):
    variables = getVariables(request)
    resp = {}
    user = get_object_or_404(User, pk=user_id)
    resp.update({f'user_{user.id}': model_to_dict(user)})

    projs = Project.objects.filter(parent_obj=user)
    projs_dict = {}
    for proj in projs:
        projs_dict.update({f'proj_{proj.id}': model_to_dict(proj)})

    resp.update({'projs': projs_dict})

    return JsonResponse(resp)


def Project__(request, user_id):
    resp = manipulate_TODO_objects(request, Project, user_id)
    return JsonResponse(resp)


def getproject(request, user_id, proj_id):
    variables = getVariables(request)
    projs = Project.objects.filter(parent_obj=user_id)

    proj = None
    list_ = None
    lists = None
    resp = {}

    for proj_ in projs:
        if proj_.id == proj_id:
            proj = proj_
            resp.update({'Project': model_to_dict(proj)})
            lists = (proj_.list_set.all())
            # print('lists_Qs', lists, 'lists_Qs')

    if proj is None:
        error = not_found_resp(projs, user_id, proj_id)
        return JsonResponse(error)

    lists_dict = {}
    for lis in lists:
        # if lis.id == list_id:
        list_ = lis
        lists_dict.update({'List_' + str(lis.id): model_to_dict(lis)})
        # print('lists', resp, 'lists')
    resp.update({'Lists': lists_dict})

    return JsonResponse(resp)


def List__(request, user_id, proj_id):
    resp = manipulate_TODO_objects(request, List, user_id, proj_id)
    return JsonResponse(resp)


def getlist(request, user_id, proj_id, list_id):
    variables = getVariables(request)
    print(f'getlist({request}, {user_id}, {proj_id}, {list_id})')
    projs = Project.objects.filter(parent_obj=user_id)

    proj = None
    list_ = None
    lists = None
    task_ = None
    tasks = None
    resp = {}

    for proj_ in projs:
        if proj_.id == proj_id:
            proj = proj_
            # resp.update({'Project': model_to_dict(proj)})
            lists = (proj_.list_set.all())
            # print('lists_Qs', lists, 'lists_Qs')

    if proj is None:
        error = not_found_resp(projs, user_id, proj_id)
        return JsonResponse(error)

    lists_dict = {}
    for lis in lists:
        if lis.id == list_id:
            list_ = lis
            lists_dict.update({'List': model_to_dict(lis)})
            tasks = (lis.task_set.all())
            # print('lists', resp, 'lists')
    resp.update(lists_dict)

    if list_ is None:
        error = not_found_resp(lists, user_id, proj_id, list_id)
        return JsonResponse(error)

    tasks_dict = {}
    for tas in tasks:
        # if tas.id == task_id:
        task_ = tas
        tasks_dict.update({'Task': model_to_dict(tas)})
        # print('tasks', resp, 'tasks')

    resp.update(tasks_dict)

    if task_ is None:
        error = not_found_resp(tasks, user_id, proj_id, list_id)
        return JsonResponse(error)

    return JsonResponse(resp)


def Task__(request, user_id, proj_id, list_id):
    resp = manipulate_TODO_objects(request, Task, user_id, proj_id, list_id)
    return JsonResponse(resp)


def gettask(request, user_id, proj_id, list_id, task_id):
    variables = getVariables(request)
    projs = Project.objects.filter(parent_obj=user_id)

    proj = None
    list_ = None
    lists = None
    tasks = None
    task_ = None
    resp = {}

    for proj_ in projs:
        if proj_.id == proj_id:
            proj = proj_
            # resp.update({'Project': model_to_dict(proj)})
            lists = (proj_.list_set.all())
            # print('lists_Qs', lists, 'lists_Qs')

    if proj is None:
        error = not_found_resp(projs, user_id, proj_id)
        return JsonResponse(error)

    lists_dict = {}
    for lis in lists:
        if lis.id == list_id:
            list_ = lis
            # lists_dict.update({'List': model_to_dict(lis)})
            tasks = (lis.task_set.all())
            # print('lists', resp, 'lists')
    resp.update(lists_dict)

    if list_ is None:
        error = not_found_resp(lists, user_id, proj_id, list_id)
        return JsonResponse(error)

    tasks_dict = {}
    for tas in tasks:

        if tas.id == task_id:
            task_ = tas
            tasks_dict.update({'Task': model_to_dict(tas)})
            # print('tasks', resp, 'tasks')

    resp.update(tasks_dict)

    if task_ is None:
        error = not_found_resp(tasks, user_id, proj_id, list_id)
        return JsonResponse(error)

    return JsonResponse(resp)


"""http://{host}/todo/{ vars/ , all/ , }"""


def vars(request):
    return JsonResponse(getVariables(request))


def getAll(request):
    resp = {}

    if request.GET.get('users'):
        users = User.objects.all()
        for user in users:
            resp.update({f"User_{user.id}": model_to_dict(user)})

    elif request.GET.get('projects'):
        projects = Project.objects.all()
        for project in projects:
            resp.update({f"Project_{project.id}": model_to_dict(project)})

    elif request.GET.get('lists'):
        lists = List.objects.all()
        for list in lists:
            resp.update({f"List_{list.id}": model_to_dict(list)})

    elif request.GET.get('tasks'):
        tasks = Task.objects.all()
        for task in tasks:
            resp.update({f"Task_{task.id}": model_to_dict(task)})

    else:
        everything = getEverything(request)
        resp.update(everything)

    return JsonResponse(resp)


def getUser(request, user_id):
    user = User.objects.get(pk=user_id)

    projs = Project.objects.filter(parent_obj=user)
    projs_DICT = {}
    for proj in projs:

        lists = List.objects.filter(parent_obj=proj)
        lists_DICT = {}
        for list in lists:

            tasks = Task.objects.filter(parent_obj=list)
            tasks_DICT = {}
            for task in tasks:
                tasks_DICT.update({f"Task_{task.id}": model_to_dict(task)})

            list_d = model_to_dict(list)
            list_d.update({"Tasks": tasks_DICT})
            lists_DICT.update({f"List_{list.id}": list_d})

        proj_d = model_to_dict(proj)
        proj_d.update({"Lists": lists_DICT})
        projs_DICT.update({f"Project_{proj.id}": proj_d})

    user_DICT = model_to_dict(user)
    user_DICT.update({"Projects": projs_DICT})

    return JsonResponse(user_DICT)


def getEverything(request):
    users = User.objects.all()
    user_DICT = {}
    for user in users:

        projs = Project.objects.filter(parent_obj=user)
        projs_DICT = {}
        for proj in projs:

            lists = List.objects.filter(parent_obj=proj)
            lists_DICT = {}
            for list in lists:

                tasks = Task.objects.filter(parent_obj=list)
                tasks_DICT = {}
                for task in tasks:
                    tasks_DICT.update({f"Task_{task.id}": model_to_dict(task)})

                list_d = model_to_dict(list)
                list_d.update(tasks_DICT)
                lists_DICT.update({f"List_{list.id}": list_d})

            proj_d = model_to_dict(proj)
            proj_d.update(lists_DICT)
            projs_DICT.update({f"Project_{proj.id}": proj_d})

        user_d = model_to_dict(user)
        user_d.update(projs_DICT)
        user_DICT.update({f"User_{user.id}": user_d})

    return user_DICT
