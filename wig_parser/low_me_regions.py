#!/usr/bin/env python3

import sys
import wig_parser as wp
import statistics

def main():
    main_list = wp.parse_wig(sys.argv[1])
    windows = filter_win(main_list, width = int(sys.argv[2]), real_width_min = int(sys.argv[3]), ts = float(sys.argv[4]))
    print_wins(windows, sys.stdout)

def filter_win(wig, width = 100, real_width_min = 10000, ts = 0.2):
    good_wins = []
    cur_win = []
    for section in wig["sections"]:
        for wig_entry in section["entries"]:
            wig_entry["chromosome_name"] = section["chromosome_name"]
            wig_entry["file_path"] = section["file_path"]
            if len(cur_win) >= width:
                to_remove = len(cur_win) - width + 1
                cur_win  = cur_win[to_remove:]
            cur_win.append(wig_entry)
            if len(cur_win) == width and filter_one_win(cur_win, real_width_min, ts):
                good_wins.append(cur_win)
    return(good_wins)

def all_chroms_match(win):
    first_chrom = win[0]["chromosome_name"]
    for entry in win:
        if not entry["chromosome_name"] == first_chrom:
            return(False)
    return(True)

def width_above_threshold(win, real_width_min):
    start = win[0]["position"]
    end = win[-1]["position"]
    return (end - start) >= real_width_min

def get_win_avg(win):
    values = []
    for entry in win:
        values.append(entry["value"])
    avg = statistics.mean(values)
    return(avg)

def avg_below_threshold(win, threshold):
    avg = get_win_avg(win)
    return avg <= threshold

def filter_one_win(win, real_width_min, ts):
    chroms_ok = all_chroms_match(win)
    width_ok = width_above_threshold(win, real_width_min)
    avg_val_ok = avg_below_threshold(win, ts)
    return chroms_ok and width_ok and avg_val_ok

def filter_ave(average_me, width = 100, real_width_min = 10000, ts = 0.2):
    me_sum = 0
    me_ave = 0
    single_win = []
    win_list = {}
    i = 0
    j = 1
    while i <= len(average_me)-width:
        # average_me is the parsed data, including four rows: chr, pos, value and filename. len(average_me) shows us how many lines in the data.
        me_sum = average_me[i][3]
        while j <= width:
            me_sum += average_me[i+1][3]
            j += 1
        me_ave = me_sum/width
        if me_ave <= ts:
            single_win.append(average_me[i][0])  # chromosome
            single_win.append(average_me[i][1])  # start pos
            single_win.append(average_me[i+width]) # end pos
            single_win.append(me_ave) # average methylation rate in the window.
            win_list.append(single_win)
        print(win_list)

def print_win(win, out_conn):
    out_str = "\t".join([
        win[0]["chromosome_name"],
        str(win[0]["position"]-1),
        str(win[-1]["position"]),
        str(get_win_avg(win)),
        str(win[0]["file_path"])
    ]) + "\n"
    out_conn.write(out_str)
        
def print_wins(low_me_wins, out_conn):
    for win in low_me_wins:
        print_win(win, out_conn)
    
main()

