from django.urls import path
from main import views



urlpatterns = [
	path('', views.index, name = 'index'),
	path('sign-in', views.sign_in, name = 'sign_in'),
	path('sign-out', views.sign_out, name = 'sign_out'),
	path('dashboard', views.dashboard, name = 'dashboard'),
	path('dashboard/remove/<int:id>', views.remove, name = 'remove'),
]