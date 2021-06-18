#!/usr/bin/env python3

import sys
import wig_parser as wp

def main():
    wig = wp.parse_wig(sys.argv[1])
    wp.write_wig(wig, sys.stdout)

if __name__ == "__main__":
    main()
