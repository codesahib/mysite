from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path(r'ml', views.project_ml, name='project-ml'),
    path(r'android', views.project_android, name='project-android'),
    path(r'web', views.project_web, name='project-web'),
    path(r'engg', views.project_engg, name='project-engg'),   
]