def f(*args, **kwargs):
    z = 1
    for i in args:
        print(i)
    for j in kwargs:
        print(j, kwargs[j])
print(f(1, 3, 5, 5, v = 0, f = 1))

