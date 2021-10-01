def f(a, b, c=3, d=4):
    print(a,b,c,d)
    
args = (1,2)
kwargs = {"c":5, "d": 6}

f(*args, **kwargs)