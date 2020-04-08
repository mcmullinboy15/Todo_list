from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import User, UserManager, AbstractUser, AbstractBaseUser, PermissionsMixin, \
    BaseUserManager
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from django.contrib.postgres.fields import ArrayField


# class Profile(User, PermissionsMixin):
#     """
#     An abstract base class implementing a fully featured User model with
#     admin-compliant permissions.
#
#     Username and password are required. Other fields are optional.
#     """
#     username_validator = UnicodeUsernameValidator()
#
#     username = models.CharField(
#         _('username'),
#         max_length=150,
#         unique=True,
#     help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
#     validators=[username_validator],
#     error_messages={
#         'unique': _("A user with that username already exists."),
#     },
# )
# first_name = models.CharField(_('first name'), max_length=30, blank=True)
# last_name = models.CharField(_('last name'), max_length=150, blank=True)
# email = models.EmailField(_('email address'), blank=True)
# is_staff = models.BooleanField(
#     _('staff status'),
#     default=False,
#     help_text=_('Designates whether the user can log into this admin site.'),
# )
# is_active = models.BooleanField(
#     _('active'),
#     default=True,
#     help_text=_(
#         'Designates whether this user should be treated as active. '
#         'Unselect this instead of deleting accounts.'
#     ),
# )
# date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
#
# objects = UserManager()
#
# EMAIL_FIELD = 'email'
# USERNAME_FIELD = 'username'
# REQUIRED_FIELDS = ['email']
#
# class Meta:
#     verbose_name = _('user')
#     verbose_name_plural = _('users')
#     abstract = True
#
# def clean(self):
#     super().clean()
#     self.email = self.__class__.objects.normalize_email(self.email)
#
# def get_full_name(self):
#     """
#     Return the first_name plus the last_name, with a space in between.
#     """
#     full_name = '%s %s' % (self.first_name, self.last_name)
#     return full_name.strip()
#
# def get_short_name(self):
#     """Return the short name for the user."""
#     return self.first_name
#
# def email_user(self, subject, message, from_email=None, **kwargs):
#     """Send an email to this user."""
#     send_mail(subject, message, from_email, [self.email], **kwargs)
#
#     phone = models.CharField(max_length=20)
#     _user = models.ForeignKey(User, related_name='profile_user', blank=True, null=True, on_delete=models.PROTECT)# .CASCADE)
#     # _user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"""
# ==========  Profile  ==========\n
# {self.first_name} {self.last_name}\n
# {self.email}\n
# """

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
"""


class Project(TODO_Template):
    parent_obj = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None,
                                   db_constraint=False, )  # related_name='user')

    type = 'Project'
    parent = 'User'

    def share(self, subject, message, from_email=None, **kwargs):
        """        sends an email to this User        """
        send_mail(subject, message, from_email, [self._user.email], **kwargs)

    def __str__(self):
        return f"""
==========  Project  ==========\n
{self.id}\n
{self.title}\n
{self.description}\n
{self.content}\n
{self.created}\n
{self.contributors}\n
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
"""
# {self._list}\n
# """
