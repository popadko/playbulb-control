__author__ = 'Oleg'

import os
from revision.my import MyRevision

class Bulb:

    def __init__(self, address):
        self.address = address
        self.revision = MyRevision()

    def on(self):
        self.commnd(self.revision.color(), 'FFFFFFFF')

    def off(self):
        self.commnd(self.revision.color(), '00000000')

    def commnd(self, command, value):
        os.system('gatttool -b %s --char-write -a %s -n %s' % (self.address, command, value))

if __name__ == '__main__':
    bulb = Bulb(os.getenv('PLAYBULB_ADDRESS'))
    bulb.on()