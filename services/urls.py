from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_services, name='get_services'),
]
