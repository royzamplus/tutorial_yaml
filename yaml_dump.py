#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

aproject = { 'name': 'Silenthand Olleander',
             'race': 'Human',
             'traits': [ 'ONE_HAND', 'ONE_EYE' ] 
            }

print yaml.dump(aproject)