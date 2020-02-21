from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch # Marks the base function that handles the object type
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str) # Each specialized function is decorated with @<base_function>.register(<type>)
def _(text): # The name of the specialized function is irrelevant; _ is a good choice to make this clear.
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral) # For each additional type to receive special treatement, register a new function. numbers.Integral is a virtual superclass of int.
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple) # You can stack several register decorators to support different types with the same function.
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'

'''When possible, register the specialized functions to handle ABCs (abstract classes) such as numbers.Integral and abc.MutableSequence instead of concrete implementations like int and list. 
This allows your code to support a greater variety of compatible types. For example, a Python extension can provide alternatives to the int type with fixed bit lengths as subclasses of numbers.Integral.'''