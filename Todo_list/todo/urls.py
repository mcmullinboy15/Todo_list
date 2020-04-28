import django
from django.urls import path, include
from . import views
from . import views_api

from django.contrib.auth import views as auth_views

app_name = 'todo'


""" /todo/<int:user_id>/api/ :: project/ """
api_urlpatterns = [

    path('', views_api.getUser, name='getUser'),
    path('project/', views_api.Project__, name='project_list'),
    path('project/<int:proj_id>/', views_api.getproject, name='lists'),  # def project_list calls project without all
    path('project/<int:proj_id>/list/', views_api.List__, name='_lists'),
    path('project/<int:proj_id>/list/<int:list_id>/', views_api.getlist, name='tasks'),
    path('project/<int:proj_id>/list/<int:list_id>/task/', views_api.Task__, name='details'),
    path('project/<int:proj_id>/list/<int:list_id>/task/<int:task_id>/', views_api.gettask, name='details'),

]

""" /todo/<int:user_id>/api_edit/ """
api_edit_urlpatterns = [

    # path('', views.index, name='index'),
    path('get/', views_api.get, name='get'),
    path('new/', views_api.new, name='new'),
    path('link/', views_api.link, name='link'),  # unlink
    path('delete/', views_api.delete, name='delete'),
    path('reassign/', views_api.reassign, name='reassign'),
    path('add/', views_api.add, name='add'),  # add contributers, {remove host?? then call unlink} or reassign

]

""" /todo/<int:user_id>/todo/ """
ui_urlpatterns = [

    path('', views.User, name='getUser'),
    # path('project/', views.Project__, name='project_list'),
    path('project/<int:proj_id>/', views.Project, name='lists'),  # def project_list calls project without all
    # path('project/<int:proj_id>/list/', views.List__, name='_lists'),
    path('project/<int:proj_id>/list/<int:list_id>/', views.List, name='tasks'),
    # path('project/<int:proj_id>/list/<int:list_id>/task/', views.Task__, name='details'),
    path('project/<int:proj_id>/list/<int:list_id>/task/<int:task_id>/', views.Task, name='details'),

]

pre = '/todo/'
urlpatterns = [

    path('signup/', views.signup, name='signup'),  # make it create User!!!
    path('login/', views.login, name='login'),
    path('', views.User, name='index'),  # make it create User!!!
    path('api/', views_api.User__, name='api_User__'),
    path('<int:user_id>/', include(ui_urlpatterns)),
    path('<int:user_id>/todo/', include(ui_urlpatterns)),
    path('<int:user_id>/api/', include(api_urlpatterns)),
    path('<int:user_id>/api_edit/', include(api_edit_urlpatterns)),

    path('accounts/login/', auth_views.LoginView.as_view()),

    path('accounts/', include('django.contrib.auth.urls')),

    path('vars/', views_api.vars, name='vars'),
    path('all/', views_api.getAll, name='getall'),

]
