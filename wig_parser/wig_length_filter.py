#!/usr/bin/env python3

import sys
import wig_parser as wp

def more_entries_than_threshold(parsed_wig, ts = 3):
    for section in parsed_wig["sections"]:
        if len(section["entries"]) >= ts:
            return True
    return False
        

def main():
    file_list = []
    for line in sys.stdin:
        file_list.append(line.rstrip('\n'))
    
    wig_list = []
    for path in file_list:
        parsed_wig = wp.parse_wig(path)
        if more_entries_than_threshold(parsed_wig):
            wig_list.append(parsed_wig)
            # print(path)
    wp.print_wigs(wig_list)
    # with open("wig_dict.txt", "w") as outconn:
    #     outconn.write(str(wig_list))
            

if __name__ == "__main__":
    import sys
    main()