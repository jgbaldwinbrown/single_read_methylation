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

mkdir -p temp_dir/resquiggle
mkdir -p temp_dir/detect_mods
mkdir -p output
mkdir -p statistics_output

# copy all input files to resquiggle dir

cat file_list.txt | while read i ; do
    cp raw_data/${i} temp_dir/resquiggle
done

# run tombo to resquiggle all files in resquiggle dir

tombo resquiggle temp_dir/resquiggle/ ~/work/ref/GCA_002057885.1_ASM205788v1_genomic.fna \
     --processes 15 --num-most-common-errors 5 # run modified base detection

# detect mods and print output for all resquiggled files, one by one

cat file_list.txt | while read i ; do
    cp temp_dir/resquiggle/${i} temp_dir/detect_mods/input.fast5
    
    tombo detect_modifications alternative_model \
         --fast5-basedirs temp_dir/detect_mods/ \
         --statistics-file-basename statistics_output/ms_DAM_testing_${i} \
         --alternate-bases dam --processes 15 # output to genome browser compatible format

    tombo text_output browser_files \
         --fast5-basedirs temp_dir/detect_mods/ \
         --statistics-filename statistics_output/ms_DAM_testing_${i}.dam.tombo.stats \
         --file-types coverage dampened_fraction difference \
         --browser-file-basename output/ms_DAM_testing_${i}

    rm temp_dir/detect_mods/input.fast5
done

# tombo text_output browser_files \
#      --fast5-basedirs ~/work/tombo/12_02/dam/Mer2_Sss1_p/ \
#      --control-fast5-basedirs ~/work/tombo/CONTROL_DIR/ \
#      --statistics-filename ms_DAM_testing.dam.tombo.stats \
#      --file-types coverage dampened_fraction difference \
#      --browser-file-basename ms_DAM_testing_difference 

# Kewei, here's a comment for you to find!
