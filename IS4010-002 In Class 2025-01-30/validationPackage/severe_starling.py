# severe_starling.py

# Enforce no leading or trailing spaces
# Madison Geier
#geierml@mail.uc.edu


def validate_password(password):

     password = password.strip()
     if not password: 
         return False, "Password cannot be empty."
     return True, ""


     
