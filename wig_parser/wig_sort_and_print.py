#!/usr/bin/env python3

import sys
import wig_parser as wp

def sort_key(wig_object):
    return((wig_object["chromosome_number"], wig_object["entries"][0]["position"]))

def sort_wigs(wigs_list):
    sorted_wigs = sorted(
        wigs_list, 
        key = lambda x: (x["chromosome_number"], x["entries"][0]["position"])
    )
    return(sorted_wigs)

def print_wig(wig):
    for entry in wig["entries"]:
        print_list = []
        print_list.append(str(wig["chromosome_number"]))
        print_list.append(str(entry["position"]))
        print_list.append(str(entry["value"]))
        print_list.append(str(wig["file_path"]))
        print("\t".join(print_list))

def print_wigs(wigs):
    for wig in wigs:
        print_wig(wig)

wigs = wp.read_and_filter_wigs(sys.stdin)

# print_wigs(wigs)

sorted_wigs = sort_wigs(wigs)
print_wigs(sorted_wigs)
