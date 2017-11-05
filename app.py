#!/usr/bin/env python3

import json
import os.path
import sys

from nest import Nest, Thermostat, authorize

class ConfigFile:
    filename = None

    def __init__(self, filename='config.json'):
        self.filename = filename


    def read(self):
        with open(self.filename) as data_file:
            return json.load(data_file)


    def write(self, data):
        with open(self.filename, 'w') as data_file:
            json.dump(data, data_file)


    def exists(self):
        return os.path.exists(self.filename)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Missing argument: get / set')
        sys.exit(1)

    cfg_file = ConfigFile()
    config = None
    if cfg_file.exists():
        config = cfg_file.read()


    nest = None
    if config and 'access_token' in config:
        nest = Nest(access_token=config['access_token'])
    else:
        authorize()
        code = input("Enter code: ")
        nest = Nest(code=code)
        config = {'access_token': nest.access_token}
        cfg_file.write(config)

    thermostat = nest.get_thermostat()

    if sys.argv[1] == 'get':
        print('Ambient:', thermostat.ambient_temperature)
        print('Target:', thermostat.target_temperature)
    elif sys.argv[1] == 'set':
        if len(sys.argv) < 3:
            print('Missing argument: target temperature')
            sys.exit(1)
        thermostat.enable_heat(True)
        thermostat.target_temperature = float(sys.argv[2])
    elif sys.argv[1] == 'heat':
        thermostat.enable_heat(True)
    elif sys.argv[1] == 'eco':
        thermostat.enable_eco(True)
