import re

def validateString(string):
    return (len(string)>0 &  isinstance(string,str))

def validateEmail(string):
    reg = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if(validateString(string)):    
        return re.match(string.strip(), reg)
    return False
