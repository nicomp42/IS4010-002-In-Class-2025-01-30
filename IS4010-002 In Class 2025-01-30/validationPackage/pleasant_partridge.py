# pleasant_partridge.py
# Cam Shinker

# Enforce at least one special character

from validationPackage.config import *

def validate_password(pwd):
    """
    Shows if a password has at least one special character
    @param pwd: The password the user enters into the validator
    @return Boolean: True if the password has a special character and False if it doesn't
    """
    if any((special in special_characters) for special in pwd):
        return True
    else:
        return False


if __name__ == "__main__":
    pwd = "falcon47$^%*"
    validate_password(pwd)