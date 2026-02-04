from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def get_tasks(request):
    example_task = {
        'name': 'Build this app!',
        'urgent': True
    }
    return Response(example_task)

