def has_space(string):
    numspace = 0
    for char in string:
        if char.isspace():
            numspace += 1 
    if numspace > 0:
        return True
    return False    

def valid_credentials(credential):
    if not has_space(credential) and 3<=len(credential)<=20:
        return True
    return False

def valid_email(email):
    num_at = 0
    num_dot = 0
    for char in email:
        if char =="@":
            num_at +=1
        if char ==".":
            num_dot +=1
    if num_at ==1 and num_dot ==1:
        return True
    return False
