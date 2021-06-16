#!/usr/bin/env python3

import sys
def mcall_filter(filename):
    infile = open(filename, 'r')
    file = infile.readlines()
    each_line = [0,0,0,'a']
    new_list = []
    file_list = []
    for line in file:
        new_line = line.strip()
        new_line = new_line.split()
        file_list.append(new_line)
    for section in file_list:
        if section[0][3] == 'M':
            chromosome_number = 17
        else:
            chromosome_number = int(section[0][3])
        position = int(section[2])
        value = float(section[-1])
        read_name = section[1]
        each_line[0] = chromosome_number
        each_line[1] = position
        each_line[2] = value
        each_line[3] = read_name
        new_list.append(each_line)
        each_line = [0,0,0,'a']
    return new_list

def main():
    filename = sys.argv[1]
    out = mcall_filter(filename)
    for line in out:
        all_str_line = []
        for word in line:
            all_str_line.append(str(word))
        print("\t".join(all_str_line))

if __name__ == "__main__":
    main()
