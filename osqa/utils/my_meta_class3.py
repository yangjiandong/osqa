# -*- coding: utf-8 -*-
# my_meta_class3

#the metaclass will automatically get passed the same argument
#that you usually pass to 'type'
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    """
    return a class object, with the list of its attribute turned
    into uppercase.
    """

    attrs = ((name, value)for name,value in future_class_attr.items() if not name.startswith('__'))
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)

    return type(future_class_name, future_class_parents, uppercase_attr)

__metaclass__ = upper_attr

class Foo(object):
    __metaclass__ = upper_attr

    """docstring for Foo"""
    bar = 'bip'

print hasattr(Foo, 'bar')
print hasattr(Foo, 'BAR')

f = Foo()
print f.BAR
