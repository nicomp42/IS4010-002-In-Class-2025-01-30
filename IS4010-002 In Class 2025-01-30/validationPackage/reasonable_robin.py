# reasonable_robin.py
#Ryan Jacob

# Enforce at least one underscore


def validate_password(pwd):
    """
    #this function validates if there is an underscore in the password
    # @param pwd: input string to test
    # return bool: true if pwd contains underscore, false if it doesnt
    """

    if "_" in pwd:
        return True
    else:
        return False
        

    

    