#!/usr/bin/env python3

import sys
import math
import statistics

def main():
    reads = {}
    for line in sys.stdin:
        sl = line.rstrip('\n').split('\t')
        if sl[3] not in reads:
            reads[sl[3]] = []
        reads[sl[3]].append(float(sl[2]))
    reads_avg = []
    for name, meth_vals in reads.items():
        avg = statistics.mean(meth_vals)
        reads_avg.append(avg)
    bins = [0 for x in range(11)]
    for avg in reads_avg:
        bin_index = int(math.floor(avg * 10))
        bins[bin_index] += 1
    bin_indices = [0.1 * x for x in range(11)]
    for a_bin, index in zip(bins, bin_indices):
        print(index, a_bin, sep="\t")

if __name__ == "__main__":
    main()
