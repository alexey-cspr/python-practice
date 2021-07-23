def cached(func):
    temp = {}
    def wrapper(*args,**kwargs):
        var = (func, args, tuple(kwargs.items()))
        if var not in temp:
            temp[var] = func(*args, **kwargs)
            return temp[var]
        else:
            return temp[var]
    return wrapper

@cached
def multi(a, b):
    return a * b

multi(3, 4)