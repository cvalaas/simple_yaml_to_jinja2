#!/usr/bin/env python

import yaml
import argparse
from jinja2 import Environment, FileSystemLoader, Template

ENV = Environment(loader=FileSystemLoader('./'))

parser = argparse.ArgumentParser(description="Sync up XMatters with Workday")
parser.add_argument('-y', '--yaml', action='store', help='yaml file', type=str, default='input.yml')
parser.add_argument('-t', '--template', action='store', help='jinja/template file', type=str, default='template.j2')
args = parser.parse_args()

with open(args.yaml) as yaml_file:
  data = yaml.load(yaml_file)

template = ENV.get_template(args.template)
print(template.render(data=data))
