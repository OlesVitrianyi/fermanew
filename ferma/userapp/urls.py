from django.urls import path

from django.contrib.auth import views as auth_views
from . import views
from .views import *

urlpatterns = [
    path('login_user/', login_user, name='login'),
    path('logout_user/', logout_user, name='logout'),
    path('register_user/', register_user, name='register'),
]

