# severe_starling.py

# Enforce no leading or trailing spaces
# Madison Geier
#geierml@mail.uc.edu


def validate_password(password):
    if password.endswith(' ') or password.startswith(' '):
        return False
    else:
        return True
    """
     password = password.strip()
     if not password:
         return False, "Password cannot be empty."
     return True, ""
    """    


     
