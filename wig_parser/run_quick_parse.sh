#!/bin/bash

python3 quick_reparse.py ../M419_test/SD_DAM_testing_954b85a9-ef7b-476a-a48f-39926c0b97f2.fast5.fraction_modified_reads.plus.wig > temp.txt
diff ../M419_test/SD_DAM_testing_954b85a9-ef7b-476a-a48f-39926c0b97f2.fast5.fraction_modified_reads.plus.wig temp.txt
