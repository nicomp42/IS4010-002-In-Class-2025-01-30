# zesty_xenops.py
# Enforce cannot be all zeroes
# Connor Thomas
# thoma5cg@mail.uc.edu

def validate_password(password: str) -> bool:
    """
    Validates that the password is not all zeroes.
    @param: The password string to validate.
    @return: True if the password is valid. False if it consists only of zeroes.
    """
    return password.strip('0') != ''