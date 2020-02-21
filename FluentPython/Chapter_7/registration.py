registry = [] # Registry will hold references to functions decorated by @register.

def register(func): # Register takes a function as an argument
    print('running register(%s)' % func) # Display what function is being decorated, for demonstration.
    registry.append(func) # Include func in register
    return func # Return func: we must return a function; here we return the same received as argument.

@register # f1 and f2 are decorated by @register.
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3(): # f3 is not decorated.
    print('running f3()')

def main(): # Main displays the registry, then calls f1(), f2(), and f3(). 
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

if __name__=='__main__': # main() is only invoked if registration.py runs as a script.
    main()