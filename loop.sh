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
         --statistics-file-basename statistics_output/SD_DAM_testing_${i} \
         --alternate-bases dam --processes 15 # output to genome browser compatible format

    tombo text_output browser_files \
         --fast5-basedirs temp_dir/detect_mods/ \
         --statistics-filename statistics_output/SD_DAM_testing_${i}.dam.tombo.stats \
         --file-types coverage fraction \
         --browser-file-basename output/SD_DAM_testing_${i}
    rm temp_dir/detect_mods/input.fast5
done

