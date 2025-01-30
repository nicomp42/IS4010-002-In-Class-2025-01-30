# flighty_falcon.py
# Luke Elmore
# Enforce at least one capital letter

def validate_password(pwd):
    """
    It will take the password and make sure it has one capital letter in it
    @param pwd string: is the password that needs validating
    @return: True if the password is valid, false if the password is not vaild
    """
    for char in pwd:
        if char.isupper():
            return True
        else:
            return False

   