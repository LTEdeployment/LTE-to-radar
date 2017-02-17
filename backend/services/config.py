# -*- coding: utf-8 -*-
# read config
import json
import sys

with open('../config/default.json') as config_file:
    config_default = json.load(config_file)

if len(sys.argv) > 1:
    with open('../config/%s.json' % sys.argv[1]) as config_file:
        config_env = json.load(config_file)

with open('../config/local.json') as config_file:
    config_local = json.load(config_file)

config = config_default.copy()
if config_env != None:
    config.update(config_env)
config.update(config_local)
