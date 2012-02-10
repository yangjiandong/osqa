#-*- coding: utf-8 -*-#
# pylint: disable=W0401, E0202
# pylint: enable-msg=C0302

#显式的继承object
class Parrot(object):
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage
    
    #配合@property,增加setter
    @voltage.setter
    def voltage(self, new_value):
        self._voltage = new_value
        
if __name__ == "__main__":
    # instance
    p = Parrot()
    # similarly invoke "getter" via @property
    print p.voltage
    # update, similarly invoke "setter"
    p.voltage = 12
