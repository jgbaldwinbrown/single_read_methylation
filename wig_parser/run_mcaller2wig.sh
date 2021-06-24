#!/bin/bash
set -e

python3 mcaller2wig.py mcaller_file.txt read_
ls read* > list.txt
cat list.txt | python3 wig_sort_and_print.py 
