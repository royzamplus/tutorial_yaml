#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

print yaml.dump(range(50))

print yaml.dump(range(50), width=50, indent=4)

print yaml.dump(range(5), canonical=True)

print yaml.dump(range(5), default_flow_style=False)

print yaml.dump(range(5), default_flow_style=True, default_style='"')
