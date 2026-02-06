from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_tasks),
    path('users/<username>/', views.get_user, name="user"),
    path('users/', views.create_user, name="create_user"),
]