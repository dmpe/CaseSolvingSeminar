# https://github.com/Rexamine/stringi/issues/212

library(openNLP)
library(NLP)
library(rJava)
library(RWeka)
library(quanteda)
library(stringi)
library(readr)

data_n <-  readr::read_csv("~/Documents/python-notebook/raw_data/data_utf8.csv")
data_n$StringLength <- stri_length(data_n$STATUS)

for (i in 1:length(data_n$STATUS)) {
  data_n$Number_of_Words[[i]] <- stri_count_words(data_n$STATUS[i])
  data_n$Number_of_Dots[[i]] <- stri_count_fixed(data_n$STATUS[i], ".")
  data_n$Number_of_Commas[[i]] <- stri_count_fixed(data_n$STATUS[i], ",")
  data_n$Number_of_Semicolons[[i]] <- stri_count_fixed(data_n$STATUS[i], ";")
  data_n$Number_of_Colons[[i]] <- stri_count_fixed(data_n$STATUS[i], ":")
  data_n$Avarage_Word_Lenght[[i]] <- round((data.frame(t(stri_stats_latex(data_n$STATUS[i])))$CharsWord / data_n$Number_of_Words[[i]]), 3)
  data_n$Lexical_Diversity[[i]] <- round(quanteda::lexdiv(dfm(data_n$STATUS[i], verbose = F, removeNumbers = F, removePunct = F, removeSeparators = F), "TTR"), 3)
}
 
readr::write_csv(data_n, "~/Documents/python-notebook/raw_data/data_n.csv")
