#Before check senior answer, write your oun code
#Then check another solution
def only_ints(a,b):
    try:
        if type(a)==int and type(b)==int:
            return True
        return False
    except:
        return False
