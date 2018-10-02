#!/usr/bin/env python3
"""
    deadcolorful  simple dead pixel check
"""
import argparse

ARGP = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawTextHelpFormatter,
)

def main(argp=None):
    if argp is None:
        argp = ARGP.parse_args()  # pragma: no cover

    print(argp)

if __name__ == '__main__':
    main()  # pragma: no cover
