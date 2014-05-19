#!/usr/bin/env python
from __future__ import print_function
from mako.template import Template
from mako.lookup import TemplateLookup
import yaml
import argparse
import os

FILE_PATH = os.path.dirname(__file__)

TEMPLATES = ['binning/index.rst',
             'binning/setup.rst',
             'binning/concoct.rst',
             'binning/phylosift.rst']

def main(args):
    with open(os.path.join(args.input_path, "settings.yaml")) as settings_file:
        settings = yaml.load(settings_file)

    lookup = TemplateLookup(directories=[args.template_path])
    for t in TEMPLATES: 
        template = lookup.get_template(t)
        print(template.render(**settings), 
                file=open(os.path.join(args.output_path, t), 'w'))

def sanitize_input(args):
    assert os.path.isdir(args.output_path)
    assert os.path.isdir(args.input_path)
    assert os.path.isdir(args.template_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output_path', default='source/',
        help=('Path to where rendered templates will be written.'
            ' Any existing files with the same file names will '
            'be over written. Default = sources'))
    parser.add_argument('-i', '--input_path', default='mako/',
        help=('Path where the raw mako settings '
            'files are stored. Default = mako'))
    parser.add_argument('-t', '--template_path', default=None,
        help=('Path where the raw mako templates are stored. '
            'Default = <input_path>/templates'))
    args = parser.parse_args()
    if args.template_path is None:
        args.template_path = os.path.join(args.input_path, 'templates')
    sanitize_input(args)
    main(args)
