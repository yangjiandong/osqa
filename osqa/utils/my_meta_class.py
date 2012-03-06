# coding: utf-8
class ObjectCreator(object):
    pass
print ObjectCreator
def echo(o):
    print o
    
echo(ObjectCreator)
print hasattr(ObjectCreator, 'new_attribute')
ObjectCreator.new_attribute =  'foo'
print hasattr(ObjectCreator, 'new_attribute')
ObjectCreatorMirror = ObjectCreator
print ObjectCreatorMirror.new_attribute
print ObjectCreatorMirror()
print ObjectCreator()
def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar
    
MyClass = choose_class('foo')
print MyClass
print type(1)
print type("1")