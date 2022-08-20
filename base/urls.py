from django.urls import path
from . import views


# the urls.py is used to create url for a template, which can be accessed by a user, an authenticated user.

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),

    path('create-room', views.create_room, name="create-room")
]