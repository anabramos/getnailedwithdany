from . import views
from django.urls import path


urlpatterns = [
    path('', views.get_services, name='get_services'),
]