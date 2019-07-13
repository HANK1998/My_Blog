from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path(r'index/',views.index),
    url(r'^artical/(?P<artical_id>[0-9])$',views.artical_page),
    url(r'^artical/edit/$', views.artical_edit_page),
    url(r'^artical/edit/action$', views.artical_edit_page_action, name='artical_edit_page_action'),
]