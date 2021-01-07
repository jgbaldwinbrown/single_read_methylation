# re-squiggle raw reads
tombo resquiggle ~/work/tombo/12_02/dam/Mer2_Sss1_p/ ~/work/ref/GCA_002057885.1_ASM205788v1_genomic.fna \
     --processes 4 --num-most-common-errors 5 # run modified base detection

tombo detect_modifications alternative_model \
     --fast5-basedirs ~/work/tombo/12_02/dam/Mer2_Sss1_p/ \
     --statistics-file-basename ms_DAM_testing \
     --alternate-bases dam --processes 4 # output to genome browser compatible format

tombo text_output browser_files \
     --fast5-basedirs ~/work/tombo/12_02/dam/Mer2_Sss1_p/ \
     --statistics-filename ms_DAM_testing.dam.tombo.stats \
     --file-types coverage dampened_fraction \
     --browser-file-basename ms_DAM_testing 

tombo text_output browser_files \
     --fast5-basedirs ~/work/tombo/12_02/dam/Mer2_Sss1_p/ \
     --control-fast5-basedirs ~/work/tombo/CONTROL_DIR/ \
     --statistics-filename ms_DAM_testing.dam.tombo.stats \
     --file-types coverage dampened_fraction difference \
     --browser-file-basename ms_DAM_testing_difference 
