from django.urls import path
from ssh import views


urlpatterns = [
	path('', views.ping, name = 'ping'),
	path('create', views.create, name = 'create'),
	path('sources', views.source, name = 'sources'),
]