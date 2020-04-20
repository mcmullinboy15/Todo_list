from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, PermissionsMixin


class TODO_Template(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    content = models.TextField(blank=True, null=True)
    contributors = models.EmailField(max_length=200, blank=True, null=True,
                                     default=None)  # ArrayField(models.EmailField(max_length=200))
    created = models.DateTimeField()

    type = 'TODO_Template'
    parent = None

    def __str__(self):
        return f"""
==========  TODO_Template  ==========\n
{self.id}\n
{self.title}\n
{self.description}\n
{self.content}\n
{self.contributors}\n
{self.created}\n
=====================================
"""


class Project(TODO_Template):
    parent_obj = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None,
                                   db_constraint=False, )  # related_name='user')

    type = 'Project'
    parent = 'User'

    def share(self, subject, message, from_email=None, **kwargs):
        """        sends an email to this User        """
        send_mail(subject, message, from_email, [self.parent_obj.email], **kwargs)

    def __str__(self):
        return f"""
==========  Project  ==========\n
{self.id}\n
{self.title}\n
{self.description}\n
{self.content}\n
{self.created}\n
{self.contributors}\n
===============================
"""


# {self._user}\n
# """


class List(TODO_Template):
    parent_obj = models.ForeignKey(Project, on_delete=models.CASCADE, )  # related_name='project')

    type = 'List'
    parent = 'Project'

    def __str__(self):
        return f"""
==========  List  ==========\n
{self.id}\n
{self.title}\n
{self.description}\n
{self.created}\n
{self.content}\n
{self.contributors}\n
============================
"""


# {self._project}\n
# """


class Task(TODO_Template):
    parent_obj = models.ForeignKey(List, on_delete=models.CASCADE, )  # related_name='list')

    type = 'Task'
    parent = 'List'

    def __str__(self):
        return f"""
==========  Task  ==========\n
{self.id}\n
{self.title}\n
{self.description}\n
{self.content}\n
{self.contributors}\n
{self.created}\n
============================
"""
# {self._list}\n
# """
