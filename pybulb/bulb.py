__author__ = 'Oleg'

import os
from revision.my import MyRevision

class Bulb:

    _is_on = False

    def __init__(self, address):
        self.address = address
        self.revision = MyRevision()

    def on(self):
        self.commnd(self.revision.color(), 'FFFFFFFF')
        self._is_on = True

    def off(self):
        self.commnd(self.revision.color(), '00000000')
        self._is_on = False

    def is_on(self):
        return self._is_on

    def commnd(self, command, value):
        os.system('gatttool -b %s --char-write -a %s -n %s' % (self.address, command, value))
