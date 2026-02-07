from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import Http404
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password
from base.models import CustomUser, ProductiveObject
from base.helpers.validators import validateString, validateEmail, validateUser

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
            password=make_password(request.data.get("password")), # Password doesn't get hashed.
            email=request.data.get("email")
        )
    except IntegrityError:
        return Response("User already exists? Email already exists?")
    return Response(f"User {user.username} created successfully ")
    
@api_view(["POST"])
def productivity_gain(request):
    try:
        user = CustomUser.objects.get(username=request.data.get("username"))
        user_freetime = user.freetime.total_seconds()
        task = ProductiveObject.objects.get(user=user)
        task_duration = task.duration.total_seconds()
        productivity_gained = (task_duration/user_freetime)
        user.productivity = productivity_gained
    except CustomUser.DoesNotExist:
        raise Http404("User does not exist :(")
    return Response(f"${user.username} gained ${productivity_gained}.")

# For now, we are fetching using the id, but maybe we would need to fetch using the name?
@api_view(["GET"])
def get_productive_object(request, id):
    try:
        productive_object = ProductiveObject.objects.get(id=id)
    except ProductiveObject.DoesNotExist:
        raise Http404("Object does not exist :(")

@api_view(["POST"])
def create_productive_object(request):
    parent = validateUser(request.data.get("user"))
    productive_object = ProductiveObject.objects.create(
        user=parent,
        name=request.data.get("name"),
        productivity_value=request.data.get("productivity_value"),
        duration=request.data.get("duration")
    )
    return Response(f"${productive_object} was successfully created.")

# To Do
# Write api endpoints for ProductiveObject (GET and POST)
# Write a getter for CustomUser

# curl -X POST http://localhost:8000/productivity/gain \
#   -H "Content-Type: application/json" \
#   -d '{
#     "user": 6,
#     "name": "Deep Work Session",
#     "productivity_value": 82.5,
#     "duration": "PT1H15M"
#   }'