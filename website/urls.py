from . import views
from django.urls import path


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact-us', views.contact_us, name='contact-us'),
]