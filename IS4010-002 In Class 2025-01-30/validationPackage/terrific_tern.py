# terrific_tern.py
# BainesBro
# bainesct@mail.uc.edu
# Enforce cannot be the word PASSWORD, any combination of upper or lower case

def validate_password(pwd):
    if "password" in pwd.lower():
        return False
    return True