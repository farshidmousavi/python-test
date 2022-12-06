#i didn't check Big(O), so what you think?

def only_ints(a,b):
    try:
        if int(a+b):
            return True
        else:
            return False
    except:
        return False
