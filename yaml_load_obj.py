#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

r = yaml.load("""
none: [~, null]
bool: [true, false, on, off]
int: 42
float: 3.14159
list: [LITE, RES_ACID, SUS_DEXT]
dict: {hp: 13, sp: 5}
""")

print r

class Hero:
    def __init__(self, name, hp, sp):
        self.name = name
        self.hp = hp
        self.sp = sp

    def __repr__(self):
        return "%s(name=%r, hp=%r, sp=%r)" % (
            self.__class__.__name__, self.name, self.hp, self.sp)

r = yaml.load("""
!!python/object:__main__.Hero
name: Welthyr Syxgon
hp: 1200
sp: 0
""")

print r