#!/usr/bin/env Rscript

library(ggplot2)


my_data = read.table("wig_out.txt", sep="\t")
colnames(my_data) = c("chr", "pos", "value", "file")
# head(data)

my_data$shift_pos = my_data$pos

file_names = levels(my_data$file)

for (file_name in file_names) {
    file_data = my_data[my_data$file == file_name, ]
    file_approx = as.data.frame(approx(file_data$pos, file_data$value, rule=2, method="linear"))
    file_approx$chrom = file_data$chrom[1]
    file_approx$file = file_data$file[1]
    file_approx$fft = Re(fft(file_approx$y))
    print(head(file_approx))
    
    pdf(paste(file_approx$file[1], "_fft.pdf", sep=""))
    
    my_plot = ggplot(data = file_approx, aes(x = x, y = fft)) +
        geom_point() +
        geom_line() +
        facet_wrap(.~file, ncol=1)
    print(my_plot)
    
    dev.off()
    
    # min_value = min(file_values)
    # new_file_values = file_values - min_value
    # my_data$shift_pos[my_data$file==file_name] = new_file_values
}

# pdf("wig_out.pdf", height=6, width=8)
# 
# my_plot = ggplot(data = my_data, aes(x = shift_pos, y = value)) +
#     geom_point() +
#     geom_line() +
#     facet_wrap(.~file)
# 
# print(my_plot)
# 
# pdf("wig_out_linear.pdf", height=10, width=8)
# 
# my_plot = ggplot(data = my_data, aes(x = shift_pos, y = value)) +
#     geom_point() +
#     geom_line() +
#     facet_wrap(.~file, ncol=1)
# 
# print(my_plot)
# 
# dev.off()
# 
# pdf("wig_out_linear_truepos.pdf", height=10, width=8)
# 
# my_plot = ggplot(data = my_data, aes(x = pos, y = value)) +
#     geom_point() +
#     geom_line() +
#     lims(x=c(400000, 430000)) +
#     facet_wrap(.~file, ncol=1)
# 
# print(my_plot)
# 
# dev.off()
