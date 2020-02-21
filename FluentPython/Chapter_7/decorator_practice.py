def deco(func):
    def inner():
        print('running inner()')
    return inner # deco returns its inner function object.

@deco
def target(): # target is decorated by deco.
    print('running target()')

target() # Invoking the decorated target actually runs inner.
print(target)