#!/usr/bin/env python3

import sys
import wig_parser as wp

files = [x.rstrip('\n') for x in sys.stdin]
wigs = []
for path in files:
    wigs.append(wp.parse_wig(path))
print(wigs)
