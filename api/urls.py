from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_tasks),
    path('users/<username>/', views.get_user, name="user"),
    path('users/register', views.create_user, name="create_user"),
    path('productivity/<id>', views.get_productive_object, name="get_productive_object"),
    path('productivity/gain', views.productivity_gain, name="productivity_gain"),
    path('productivity/create', views.create_productive_object, name = "create_productivity_object")
]