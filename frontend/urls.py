from django.urls import path,include

from .views import *

urlpatterns = [
    path('', index,  name='index'),
    path('about/', about, name='about'),
    path('history/', history, name='history'),
    path('donation/', donation, name='donation'),
    path('member/', member, name='member'),
    path('contact/', contact, name='contact'),
]