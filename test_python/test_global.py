def test():
    b = 6
    x = []
    a = 100
    def inner():
        nonlocal b
        x.append(1)
        b = 1000
        print(b)
    inner()
    print(b)
    return inner
t = test()

print(t.__code__.co_varnames)
print(t.__code__.co_freevars)


