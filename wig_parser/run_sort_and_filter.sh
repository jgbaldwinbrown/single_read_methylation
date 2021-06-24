#!/bin/bash
set -e

cat list.txt | python3 wig_sort_and_print.py 100
