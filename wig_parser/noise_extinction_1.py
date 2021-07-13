#!/usr/bin/env python3

import sys


def noise_extinction_1(filename, win_length = 2000):
    old_string = 'a'
    new_list = []
    new_new_list = []
    with open(filename) as f:
        previous = None
        current = next(f).strip()
        for line in f:
            if line == None:
                line = '0 0 0 a'
            if previous == None:
                previous = '0 0 0 a'
            current = current.split()
            previous = previous.split()
            line = line.split()
            if line[3] != old_string:
                current[2] = current[2]
            elif line[3] == old_string:
                if ((float(line[2]) != 0) and (int(line[1]) - int(current[1]) <= win_length)) or ((float(previous[2]) != 0) and (int(current[1]) - int(previous[1]) <= win_length)):
                    current[2] = current[2]
                else:
                    current[2] = str(0)
            new_list.append(current)
            old_string = current[3]
            previous = listToString(current)
            current = listToString(line)
            
    for sub_list in new_list:
        sub_list[0] = int(sub_list[0])
        sub_list[1] = int(sub_list[1])
        sub_list[2] = float(sub_list[2])
        new_new_list.append(sub_list)
    return new_new_list





def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))





def main():
    filename = sys.argv[1]
    out = noise_extinction_1(filename)
    for line in out:
        all_str_line = []
        for word in line:
            all_str_line.append(str(word))
        print("\t".join(all_str_line))





if __name__ == "__main__":
    main()

