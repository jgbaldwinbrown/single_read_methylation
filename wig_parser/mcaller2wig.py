#!/usr/bin/env python3

import sys
import wig_parser as wp

def main():
    wig = wp.mcaller_to_wig(sys.argv[1])
    prefix = sys.argv[2]
    for one_wig in wig:
        with open(prefix + one_wig["file_path"], "w") as output:
            wp.write_wig(one_wig, output)

if __name__ == "__main__":
    main()
