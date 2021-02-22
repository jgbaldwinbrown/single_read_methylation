#!/usr/bin/env Rscript

library(ggplot2)


my_data = read.table("wig_out.txt", sep="\t")
colnames(my_data) = c("chr", "pos", "value", "file")
# head(data)

my_data$shift_pos = my_data$pos

file_names = levels(my_data$file)

for (file_name in file_names) {
    file_values = my_data$pos[my_data$file == file_name]
    min_value = min(file_values)
    new_file_values = file_values - min_value
    my_data$shift_pos[my_data$file==file_name] = new_file_values
}

pdf("wig_out.pdf", height=6, width=8)

my_plot = ggplot(data = my_data, aes(x = shift_pos, y = value)) +
    geom_point() +
    geom_line() +
    facet_wrap(.~file)

print(my_plot)

pdf("wig_out_linear.pdf", height=10, width=8)

my_plot = ggplot(data = my_data, aes(x = shift_pos, y = value)) +
    geom_point() +
    geom_line() +
    facet_wrap(.~file, ncol=1)

print(my_plot)

dev.off()

pdf("wig_out_linear_truepos.pdf", height=10, width=8)

my_plot = ggplot(data = my_data, aes(x = pos, y = value)) +
    geom_point() +
    geom_line() +
    lims(x=c(400000, 430000)) +
    facet_wrap(.~file, ncol=1)

print(my_plot)

dev.off()
