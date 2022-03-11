from . import views
from django.urls import path


urlpatterns = [
    path('make-appointment', views.make_appointment, name='make-appointment'),
]