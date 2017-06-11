#!/usr/bin/env python
from __future__ import print_function
import sys
import argparse
import csv
import os.path
import logging
from collections import defaultdict
from signal import signal, SIGPIPE, SIGINT, SIG_DFL
signal(SIGPIPE, SIG_DFL)
signal(SIGINT, SIG_DFL)


def extant_file(x):
    """
    'Type' for argparse - checks that file exists but does not open.
    """
    if not os.path.exists(x):
        # Argparse uses the ArgumentTypeError to give a rejection message like:
        # error: argument input: x does not exist
        raise argparse.ArgumentTypeError("{0} does not exist".format(x))
    return x


def init_logger(args):
    logger = logging.getLogger(__name__)
    ch = logging.StreamHandler()
    if args.debug:
        logger.setLevel(logging.DEBUG)
        ch.setLevel(logging.DEBUG)
    elif args.verbose:
        logger.setLevel(logging.INFO)
        ch.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.WARNING)
        ch.setLevel(logging.WARNING)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return(logger)


def run_argparse():
    parser = argparse.ArgumentParser(
        description='This is a test description.')
    parser.add_argument(
        'infile', help='Input file', type=extant_file)
    parser.add_argument(
        '--debug', help='Turn on debugging messages.', action='store_true')
    parser.add_argument(
        '--verbose', help='Print verbose progress messages.',
        action='store_true')
    args = parser.parse_args()
    args.logger = init_logger(args)
    return args


def main():
    args = run_argparse()


if __name__ == '__main__':
    main()
