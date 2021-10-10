def debug_control(*args, **kwargs):
    s,i,f=0,0,0
    for idx, arg in enumerate(args):
        if type(arg) == str:
            s+=1
        elif type(arg) == int:
            i+=1
        elif type(arg) == float:
            f+=1
    for key, kwarg in kwargs.items():
        if type(key) == str:
            s += 1
        elif type(key) == int:
            i += 1
        elif type(key) == float:
            f += 1
    good = "str: "+str(s)+", int: "+str(i)+", float: "+str(f)
    return good

