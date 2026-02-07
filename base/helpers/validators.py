import re
from django.http import Http404
from ..models import CustomUser

def validateString(string):
    return (len(string)>0 &  isinstance(string,str))

def validateEmail(string):
    reg = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if(validateString(string)):    
        return re.match(string.strip(), reg)
    return False

def validateUser(id):
    try:
        user = CustomUser.objects.get(id=id)
    except CustomUser.DoesNotExist:
        raise Http404("User does not exist :(")
    return user