#!/usr/bin/env python3

import sys
import wig_parser as wp

def sort_key(wig_object):
    return((wig_object["chromosome_number"], wig_object["entries"][0]["position"]))

def sort_wigs(wigs_list):
    sorted_wigs = sorted(
        wigs_list, 
        key = lambda x: (x["sections"][0]["chromosome_number"], x["sections"][0]["entries"][0]["position"])
    )
    return(sorted_wigs)

def print_wig(wig):
    for section in wig["sections"]:
        for entry in section["entries"]:
            print_list = []
            print_list.append(str(section["chromosome_number"]))
            print_list.append(str(entry["position"]))
            print_list.append(str(entry["value"]))
            print_list.append(str(section["file_path"]))
            print("\t".join(print_list))

def print_wigs(wigs):
    for wig in wigs:
        print_wig(wig)


def main():
    wigs = wp.read_and_filter_wigs(sys.stdin)
    sorted_wigs = sort_wigs(wigs)
    print_wigs(sorted_wigs)


if __name__ == "__main__":
    import sys
    main()