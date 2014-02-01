#!/usr/bin/env python3

import sys
from argparse import ArgumentParser


def justify(text, width):
    pass

if __name__ == '__main__':
    cmd_parser = ArgumentParser(
        description='This program justified your text')
    cmd_parser.add_argument(
        '-i', '--input', dest='input',
        help='input file (required)', metavar='FILE')
    cmd_parser.add_argument(
        '-o', '--output', dest='output',
        help='output file', metavar='FILE')
    cmd_parser.add_argument(
        '-w', '--width', dest='width', default='60',
        type=int, help='string width (default: %(default)s)',
        metavar='NUMBER')
    args = cmd_parser.parse_args()

    if not args.input:
        cmd_parser.error('Input file required')
        sys.exit(1)

    try:
        with open(args.input) as in_file:
            pass
    except IOError as err:
        print(err)  # hide python traceback
        sys.exit(1)