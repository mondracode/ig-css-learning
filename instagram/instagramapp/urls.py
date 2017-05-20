from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^crear_usuario/$', views.crear_usuario, name = 'crear_usuario'),
    url(r'^home/$', views.home, name = 'home'),
    url(r'^login/$', views.login, name = 'login'),
    url(r'^perfil/$', views.perfil, name = 'perfil'),
    url(r'^buscar/$', views.buscar, name = 'buscar'),

]
