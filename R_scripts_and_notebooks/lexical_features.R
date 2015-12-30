# library(openNLP)
# library(NLP)
# library(rJava)
# library(RWeka)
library(stringi)
library(readr)

data_n <-  readr::read_csv("~/Documents/python-notebook/data_utf8.csv")
data_n$StringLength <- stri_length(data_n$STATUS)

for(i in 1:length(data_n$STATUS)) {
  data_n$Number_of_Words[[i]] <- data.frame(t(stri_stats_latex(data_n$STATUS[i])))$Words
  data_n$Number_of_Dots[[i]] <- stri_count_fixed(data_n$STATUS[i], ".")
  data_n$Number_of_Commas[[i]] <- stri_count_fixed(data_n$STATUS[i], ",")
  data_n$Number_of_Semicolons[[i]] <- stri_count_fixed(data_n$STATUS[i], ";")
  data_n$Number_of_Colons[[i]] <- stri_count_fixed(data_n$STATUS[i], ":")
}
 

