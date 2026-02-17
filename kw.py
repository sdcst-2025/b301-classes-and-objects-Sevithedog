def f(**kwargs):
    print(kwargs)
    for k in kwargs:
        print(k,kwargs[k])


f(x=3,y=4,z="hello")

f()