
from django.urls import path
from django.contrib import admin
from django.urls import include
from rango import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'rango/', include('rango.urls')),
    path(r'admin/', admin.site.urls),
]

