#!/usr/bin/env python3

import sys
def mcaller_to_wig(filename):
    infile = open(filename, 'r')
    file = infile.readlines()
    my_parsed_wig_full = {}
    my_parsed_wig = []
    my_parsed_wig_full["sections"] = my_parsed_wig
    old_string = 'a'
    for line in file:
        line = line.rstrip('\t')
        line = line.split()
        if line[3] != old_string:
            my_parsed_wig.append({})
            my_parsed_wig[-1]["entries"] = []
            chromosome_name = 'chr' + line[0]
            chromosome_number_string = line[0]
            if chromosome_number_string == "M":
                chromosome_number = 17
            else:
                chromosome_number = int(chromosome_number_string)
            my_parsed_wig[-1]["file_path"] = line[3]
            my_parsed_wig[-1]["chromosome_name"] = chromosome_name
            my_parsed_wig[-1]["chromosome_number_string"] = chromosome_number_string
            my_parsed_wig[-1]["chromosome_number"] = chromosome_number
            entry = {}
            entry["position"] = int(line[1])
            entry["value"] = float(line[2])
            my_parsed_wig[-1]["entries"].append(entry)
        elif line[3] == old_string:
            entry = {}
            entry["position"] = int(line[1])
            entry["value"] = float(line[2])
            my_parsed_wig[-1]["entries"].append(entry)
        old_string = line[3]
    return([my_parsed_wig_full])


def main():
    filename = sys.argv[1]
    out = mcaller_to_wig(filename)
    print(out)



if __name__ == "__main__":
    main()

