
#!/usr/bin/env python3

import sys
def threshold(filename, ts = 0.7):
    infile = open(filename, 'r')
    file = infile.readlines()
    new_list = []
    file_list = []
    for line in file:
        new_line = line.strip()
        new_line = new_line.split()
        if float(new_line[2]) > float(ts):
            new_line[2] = new_line[2]
        else:
            new_line[2] = str(0)
        file_list.append(new_line)
    return file_list



def main():
    filename = sys.argv[1]
    ts = sys.argv[2]
    output = threshold(filename, ts)
    for line in output:
        all_str_line = []
        for word in line:
            all_str_line.append(str(word))
        print("\t".join(all_str_line))




if __name__ == "__main__":
    main()
