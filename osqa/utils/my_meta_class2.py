# coding: utf-8
MyShinyClass = type('MyShinyClass',(),{})
print MyShinyClass
print MyShinyClass()
Foo = type('Foo',(),{'bar':True})
print Foo
print Foo.bar
f= Foo()
print f
class FooChild(Foo):
    pass
FooChild = type('FooChild',(Foo,),{})
def echo_bar(self):
    print self.bar
    
FooChild = type('FooChild',(Foo,),{'echo_bar': echo_bar})
hasattr(Foo,'echo_bar')
hasattr(FooChild,'echo_bar')
my_foo=FooChild()
my_foo.echo_bar()
my_foo.bar
print my_foo