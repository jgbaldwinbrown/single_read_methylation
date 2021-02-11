#!/usr/bin/env python3

def parse_wig(path):
    my_parsed_wig = {}
    line_number = 0
    my_parsed_wig["entries"] = []
    with open(path, "r") as inconn:
        for line in inconn:
            line = line.rstrip('\n')
            split_line = line.split()
            if line_number == 0:
                my_parsed_wig["header"] = line
            elif line_number == 1:
                my_parsed_wig["encoding"] = split_line[0]
                chromosome_name = split_line[1].split('=')[1]
                chromosome_number_string = chromosome_name.replace("chr", "")
                if chromosome_number_string == "M":
                    chromosome_number = 17
                else:
                    chromosome_number = int(chromosome_number_string)
                my_parsed_wig["file_path"] = path
                my_parsed_wig["chromosome_name"] = chromosome_name
                my_parsed_wig["chromosome_number_string"] = chromosome_number_string
                my_parsed_wig["chromosome_number"] = chromosome_number
                my_parsed_wig["span"] = int(split_line[2].split('=')[1])
            else:
                if len(split_line) >= 2:
                    entry = {}
                    entry["position"] = int(split_line[0])
                    entry["value"] = float(split_line[1])
                    my_parsed_wig["entries"].append(entry)
            line_number = line_number+1
    return(my_parsed_wig)

def read_and_filter_wigs(file_containing_paths):
    paths = []
    for line in file_containing_paths:
        paths.append(line.rstrip('\n'))
    
    wigs = []
    for path in paths:
        parsed_wig = parse_wig(path)
        if len(parsed_wig["entries"]) > 0:
            wigs.append(parsed_wig)
    return(wigs)

def main():
    file_list = []
    for line in sys.stdin:
        file_list.append(line.rstrip('\n'))
    
    wig_list = []
    for path in file_list:
        parsed_wig = parse_wig(path)
        if len(parsed_wig["entries"]) > 0:
            wig_list.append(parsed_wig)
            # print(path)
    print(wig_list)
    # with open("wig_dict.txt", "w") as outconn:
    #     outconn.write(str(wig_list))
            

if __name__ == "__main__":
    import sys
    main()
