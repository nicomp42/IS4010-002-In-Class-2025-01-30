# main.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

from validationPackage import egalitarian_eagle
from validationPackage import excited_emu
from validationPackage import flighty_falcon
from validationPackage import happy_egret
from validationPackage import pleasant_partridge
from validationPackage import reasonable_robin
from validationPackage import severe_starling
from validationPackage import sprightly_sparrow
from validationPackage import terrific_tern
from validationPackage import zesty_xenops

def test_password(pwd):
    print("testing pssword:", pwd)
    exception_count = 0
    try:
        egalitarian_eagle_status = egalitarian_eagle.validate_password(pwd)
        print("egalitarian_eagle_status:", egalitarian_eagle_status)
    except:
        print("egalitarian_eagle threw an exception")
        exception_count += 1
    try:
        excited_emu_status = excited_emu.validate_password(pwd)
        print("excited_emu_status:", excited_emu_status)
    except:
        print("excited_emu threw an exception")
        exception_count += 1

    try:
        flighty_falcon_status = flighty_falcon.validate_password(pwd)
        print("flighty_falcon_status:", flighty_falcon_status)
    except:
        print("flighty_falcon threw an exception")
        exception_count += 1
    """
    try:
        happy_egret_status = happy_egret.validate_password(pwd)
        print("happy_egret_status:", happy_egret_status)
    except:
        print("happy_egret threw an exception")
        exception_count += 1
    """
    try:
        pleasant_partridge_status = pleasant_partridge.validate_password(pwd)
        print("pleasant_partridge_status:", pleasant_partridge_status)
    except:
        print("pleasant_partridge threw an exception")
        exception_count += 1

    try:
        reasonable_robin_status = reasonable_robin.validate_password(pwd)
        print("reasonable_robin_status:", reasonable_robin_status)
    except:
        print("reasonable_robin threw an exception")
        exception_count += 1

    try:
        severe_starling_status = severe_starling.validate_password(pwd)
        print("severe_starling_status:", severe_starling_status)
    except:
        print("severe_starling threw an exception")
        exception_count += 1
    """
    try:
        sprightly_sparrow_status = sprightly_sparrow.validate_password(pwd)
        print("sprightly_sparrow_status:", sprightly_sparrow_status)
    except:
        print("sprightly_sparrow threw an exception")
        exception_count += 1
    """
    try:
        terrific_tern_status = terrific_tern.validate_password(pwd)
        print("terrific_tern_status:", terrific_tern_status)
    except:
        print("terrific_tern threw an exception")
        exception_count += 1

    try:
        zesty_xenops_status = zesty_xenops.validate_password(pwd)
        print("zesty_xenops_status:", zesty_xenops_status)
    except:
        print("zesty_xenops threw an exception")
        exception_count += 1

    print("Total exceptions thrown:", exception_count)
    if exception_count > 0:
        print("The password test could not be completed")
        return None
    
    if (    egalitarian_eagle_status 
        and excited_emu_status 
        and flighty_falcon_status 
        and pleasant_partridge_status 
        and reasonable_robin_status 
        and severe_starling_status 
        and terrific_tern_status 
        and zesty_xenops_status):
    
        return True
    else:
        return False

if __name__ == "__main__":
    pass_count = 0
    fail_count = 0
    unable_to_test_count = 0
    failed_pwds = []
    passed_pwds = []
    untestable_pwds = []
    tests = [
        ["!Aa00000_", True],          # OK
        ["!A1_", False],              # Too Short
        ["!Aa0000000000000_", False], # Too long
        ["!aaaaa_", False],           # No capital letter
        ["!AAAAAA_", False],          # No lower case letter
        ["Aaaaaaa_", False],          # No special character
        [" !Aaaaaa_", False],         # leading space
        ["!Aa aaaa_", False],         # Embedded space
        ["PASSWORD", False],          # Can't be the word PASSWORD
        ["0000000000", False]         # Can't be all zeroes
        ]
    for test in tests:
        print("***************************")
        expected_status = test[1]
        pwd = test[0]
        status = test_password(pwd)
        if status != None:
            if (status == expected_status):
                print(pwd, "Passed")
                pass_count += 1
                passed_pwds.append(pwd)
            else:
                print(pwd, "FAILED")
                fail_count += 1
                failed_pwds.append(pwd)
        else:
            unable_to_test_count += 1
            untestable_pwds.append(pwd)
    print(pass_count, "tests passed")
    print(passed_pwds)
    print(fail_count, "tests failed")
    print(failed_pwds)
    print(unable_to_test_count, "tests were unable to complete.")
    print(untestable_pwds)