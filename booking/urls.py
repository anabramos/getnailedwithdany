from django.urls import path
from . import views


urlpatterns = [
    path('make-appointment', views.make_appointment, name='make-appointment'),
    path('my-account', views.my_account, name='my-account'),
    path('edit/<appointment_appointment_id>', views.change_appointment, name='edit')
]
