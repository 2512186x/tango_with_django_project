from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path(r'^$', views.index, name='index'),
    path(r'^about/$', views.about, name='about'),
    path(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
]