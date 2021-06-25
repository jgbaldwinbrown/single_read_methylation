#!/usr/bin/env python3

import sys
import wig_parser as wp

def meth_prop_and_sums(wig_data, threshold = 0.5):
    # wig_data contains the entries "header", "entries", "encoding", "chromosome_name", "chromosome_number_string", and "chromosome_number"
    total_methylated_sites = 0
    total_sites = 0
    for section in wig_data["sections"]:
        for entry in section["entries"]:
            total_sites = total_sites + 1
            if entry["value"] >= threshold:
                total_methylated_sites += 1
    methylation_proportion = (total_methylated_sites / total_sites)
    return(methylation_proportion, total_methylated_sites, total_sites)

def grand_total_meth_prop_and_sums(meth_props_and_sums_list):
    total_methylated_sites = 0
    total_sites = 0
    for entry in meth_props_and_sums_list:
        total_methylated_sites += entry[1]
        total_sites += entry[2]
    methylation_proportion = (total_methylated_sites / total_sites)
    return(methylation_proportion, total_methylated_sites, total_sites)

# stdin should be a list of .wig files, one file path per line

def main():
    wigs = wp.read_and_filter_wigs(sys.stdin)
    proportions = []
    length_threshold = int(sys.argv[1])
    me_threshold = float(sys.argv[2])
    for wig in wigs:
        if wp.more_entries_than_threshold(wig, length_threshold):
            proportions.append(meth_prop_and_sums(wig))
        grand_totals = grand_total_meth_prop_and_sums(proportions)
    print(grand_totals)

if __name__ == "__main__":
    import sys
    main()
