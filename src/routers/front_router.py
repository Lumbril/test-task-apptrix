from django.urls import path
from api.views.front_view import *

urlpatterns = [
    path('create', create_page),
    path('list', list_page),
]
