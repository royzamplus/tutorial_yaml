#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

for data in yaml.load_all(open('documents.yaml')):
    print data