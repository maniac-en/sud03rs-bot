#!/usr/bin/env python3
import json

config_path = "config/config.json"
strings_path = "config/strings.json"

with open(config_path) as config_file, \
     open(strings_path) as strings_file:

    config_data = json.load(config_file)
    config_file.close()

    strings_data = json.load(strings_file)
    strings_file.close()


def get_config(key):
    return config_data[key]

def get_string(key):
    return strings_data[key]
