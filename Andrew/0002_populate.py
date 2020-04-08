# This file was created by running this command:
#   python manage.py makemigrations --empty polls --name populate

from django.db import migrations
from django.utils import timezone

from django.db import transaction
from django.contrib.auth.models import User, UserManager


def populate_db(apps, schema_editor):
    # Profile = apps.get_model('todo', 'Profile')
    TODO_Template = apps.get_model('todo', 'TODO_Template')
    Project = apps.get_model('todo', 'Project')
    List = apps.get_model('todo', 'List')
    Task = apps.get_model('todo', 'Task')

    # usr = User(
    #     email='McMullinboy15@gmail.com',
    #     first_name='Andrew',
    #     last_name='McMullin',
    #     date_joined=timezone.now(),
    #     is_active=True,
    # )
    # usr.save()

    usr = User.objects.create_user('mcmullin', email='mcmullin@gmail.com', password='Mcmullin15')
    # usr.is_superuser = True
    # usr.is_staff = True
    usr.save()
    print(type(usr))

    p = Project(
        title='First Project',
        description='this first project has a description',
        created=timezone.now(),
        content='This is the content of the Project 1',
        contributors='mcmullinboy1@gmail.com',
        _user=usr
    )
    p.save()

    l = List(
        title='First List',
        description='this first list has a description',
        created=timezone.now(),
        content='This is the content of the List 1',
        contributors='mcmullinand@gmail.com',
        _project=p
    )
    l.save()

    t = Task(
        title='First Task',
        description='this first Task has a description',
        created=timezone.now(),
        content='This is the content of the Task 1',
        _list=l
    )
    t.save()


    usr2 = User.objects.create_user('mcmullinboy', email='mcmullinboy@gmail.com', password='Mcmullin15')
    # usr.is_superuser = True
    # usr.is_staff = True
    usr2.save()
    print(type(usr2))


    p2 = Project(
        title='Second Project',
        description='2nd project has a description',
        created=timezone.now(),
        content='This is the content of the Project 2',
        contributors='mcmullinboy1@gmail.com',
        _user=usr2
    )
    p2.save()

    l2 = List(
        title='Second List',
        description='2nd list has a description',
        created=timezone.now(),
        content='This is the content of the List 2',
        contributors='mcmullinand@gmail.com',
        _project=p2
    )
    l2.save()

    t2 = Task(
        title='Second Task',
        description='2nd Task has a description',
        created=timezone.now(),
        content='This is the content of the Task 2',
        _list=l2
    )
    t2.save()

class Migration(migrations.Migration):
    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_db)
    ]
