#!/usr/bin/env python3

import re
import sys
from argparse import ArgumentParser


def justify(text, width):
    TEXT_INDENT = '\u00A0' * 4  # non-breaking space
    RE_SPLIT = '\n[ ]*\n'
    PARAGRAPH_SEPARAPOR = '\n\n'

    def just(text, width):
        text = text.replace('\n', ' ').strip()
        text = TEXT_INDENT + text
        lines = []
        while True:
            if len(text) <= width:
                lines.append(text)
                break
            chunk_end = text.rfind(' ', 0, width + 1)
            chunk = text[0:chunk_end].strip(' ')
            chunk_words = re.split('[ ]+', chunk)
            words_len = len(''.join(chunk_words))
            free_space_count = width - words_len
            interval_count = len(chunk_words) - 1
            spaces_on_each = free_space_count // interval_count
            free_space_count -= spaces_on_each * interval_count
            if free_space_count:
                offset = (interval_count - free_space_count) // 2
                while free_space_count:
                    index = free_space_count + offset
                    chunk_words[index] += ' '
                    free_space_count -= 1
            line = (' ' * spaces_on_each).join(chunk_words)
            lines.append(line)
            slice_start = chunk_end + 1
            text = text[slice_start::]
        return '\n'.join(lines)

    return PARAGRAPH_SEPARAPOR.join(
        [just(t, width) for t in re.split(RE_SPLIT, text)])


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
        '-w', '--width', dest='width', default=60,
        type=int, help='string width (default: %(default)s)',
        metavar='NUMBER')
    args = cmd_parser.parse_args()

    if not args.input:
        cmd_parser.error('Input file required')
        sys.exit(1)

    try:
        with open(args.input) as in_file:
            result = justify(in_file.read(), args.width)
        if args.output:
            with open(args.output, 'w+') as out_file:
                out_file.write(result)
        else:
            sys.stdout.write(result + '\n')
    except IOError as err:
        sys.stderr.write(str(err + '\n'))  # hide python traceback
        sys.exit(1)
