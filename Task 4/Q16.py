
#Answer: 2
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)



#Answer: prints finally code and the gives error.
#after f
#NameError: name 'f' is not defined
def a():
    try:
        f(x, 4)
    finally:
       print('after f')
    print('after f?')
a()
