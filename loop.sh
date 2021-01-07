# re-squiggle raw reads

# imagine there's a directory containing these:
# first_file.fast5
# second_file.fast5
# third_file.fast5
# file_list.txt

# file_list.txt contains:
# first_file.fast5
# second_file.fast5
# third_file.fast5

# to make file_list.txt:
# ls -d *.fast5 > file_list.txt

mkdir -p temp_dir
mkdir -p output
mkdir -p statistics_output

cat file_list.txt | while read i ; do
    cp ${i} temp_dir/input.fast5
    
    tombo resquiggle temp_dir/ ~/work/ref/GCA_002057885.1_ASM205788v1_genomic.fna \
         --processes 4 --num-most-common-errors 5 # run modified base detection
    
    tombo detect_modifications alternative_model \
         --fast5-basedirs temp_dir/ \
         --statistics-file-basename statistics_output/ms_DAM_testing_${i} \
         --alternate-bases dam --processes 4 # output to genome browser compatible format

    tombo text_output browser_files \
         --fast5-basedirs temp_dir/ \
         --statistics-filename statistics_output/ms_DAM_testing_${i}.dam.tombo.stats \
         --file-types coverage dampened_fraction difference \
         --browser-file-basename output/ms_DAM_testing_${i}
    rm temp_dir/input.fast5
done

# tombo text_output browser_files \
#      --fast5-basedirs ~/work/tombo/12_02/dam/Mer2_Sss1_p/ \
#      --control-fast5-basedirs ~/work/tombo/CONTROL_DIR/ \
#      --statistics-filename ms_DAM_testing.dam.tombo.stats \
#      --file-types coverage dampened_fraction difference \
#      --browser-file-basename ms_DAM_testing_difference 
