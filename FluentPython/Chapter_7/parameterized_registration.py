registry = set() # Registry is now a set, so adding/removing functions is faster.

def register(active=True):  # Takes an optional keyword argument.
    def decorate(func): # The decorate inner function is the actual decorator; note how it takes a function as argument.
        print('running register(active=%s)->decorate(%s)'
              % (active, func))
        if active: # Register func only if the active argument (retrieved from the closure) is True.
            registry.add(func)
        else:
            registry.discard(func) # If not active and func in registry, remove it.

        return func # Because decorate is a decorator, it must return a function
    return decorate # Register is our decorator factory, so it returns decorate.

@register(active=False) # The @register factory must be invoked as a function, with the desired parameters.
def f1():
    print('running f1()')

@register() # If no parameters are passed, register must still be called a function - @register() - i.e., to return the actual decorator, decorate.
def f2():
    print('running f2()')

def f3():
    print('running f3()')