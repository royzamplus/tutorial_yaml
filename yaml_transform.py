#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

class Dice(tuple):
    def __new__(cls, a, b):
        return tuple.__new__(cls, [a, b])
    def __repr__(self):
        return "Dice(%s, %s)" % self

d = Dice(3, 6)
print d

print 'Default representation for Dice object'
print yaml.dump(d)

def dice_representer(dumper, data):
    return dumper.represent_scalar(u'!dice', u'%sd%s' % data)

yaml.add_representer(Dice, dice_representer)

print yaml.dump({'gold': Dice(10, 6)})

def dice_constructor(loader, node):
    value = loader.construct_scalar(node)
    a, b = map(int, value.split('d'))
    return Dice(a, b)

yaml.add_constructor(u'!dice', dice_constructor)

print yaml.load("""
initial hit points: !dice 8d4
""")