from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import Http404
from django.db import IntegrityError
from base.models import CustomUser
from base.helpers.validators import validateString, validateEmail
@api_view(["GET"])
def get_tasks(request):
    example_task = {
        'name': 'Build this app!',
        'urgent': True
    }
    return Response(example_task)

@api_view(["GET"])
def get_user(request, username):
    try:
        usrname=CustomUser.objects.get(username=username)
        user = {
            'username': usrname.username,
            'email': usrname.email
        }
        return Response(user)
    except CustomUser.DoesNotExist:
        raise Http404("User does not exist :(")
    
@api_view(["POST"])
def create_user(request):
    validateString(request.data.get("username", request.data.get("password")))
    validateEmail(request.data.get("email"))
    try:
        user = CustomUser.objects.create(
            username=request.data.get("username"),
            password=request.data.get("password"), # Password doesn't get hashed.
            email=request.data.get("email")
        )
    except IntegrityError:
        return Response("User already exists? Email already exists?")
    return Response(f"User {user.username} created successfully ")
    