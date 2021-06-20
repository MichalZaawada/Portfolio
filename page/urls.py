from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('post/ajax/nav', views.nav, name='nav'),
    path('post/ajax/aboutme', views.change, name='aboutme'),
    path('post/ajax/contact', views.contact, name='contact'),
    path('post/ajax/projects', views.projects, name='projects'),
    path('post/ajax/index', views.index, name='index'),
    path('post/ajax/nav_en', views.nav_en, name='nav_en'),
    path('post/ajax/aboutme_en', views.change_en, name='aboutme_en'),
    path('post/ajax/contact_en', views.contact_en, name='contact_en'),
    path('post/ajax/projects_en', views.projects_en, name='projects_en'),
    path('post/ajax/index_en', views.index_en, name='index_en'),
]
