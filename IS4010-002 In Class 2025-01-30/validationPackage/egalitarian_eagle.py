# Vanshika Rana
#ranava@mail.uc.edu


# egalitarian_eagle.py

# Enforce Minimum Length Requirement

min_length = 5

def validate_password(password, min_length=5):
    if len(password) < min_length:
        return False
    return True