#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import re

class Dice(tuple):
    def __new__(cls, a, b):
        return tuple.__new__(cls, [a, b])
    def __repr__(self):
        return "Dice(%s, %s)" % self
        
pattern = re.compile(r'^\d+d\d+$')
yaml.add_implicit_resolver(u'!dice', pattern)

print yaml.dump({'treasure': Dice(10, 20)})

print yaml.load("""
damage: 5d10
""")