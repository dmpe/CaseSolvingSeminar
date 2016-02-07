# https://github.com/Rexamine/stringi/issues/212
# https://stat.ethz.ch/pipermail/r-help/2006-May/105280.html
# https://stackoverflow.com/questions/8697079/remove-all-punctuation-except-apostrophes-in-r

library(openNLP)
library(NLP)
library(RWeka)
library(RWekajars)
library(stringi)
library(stringr)
library(quanteda)
library(SnowballC)
library(methods)
library(readr)
library(Rcpp)
library(utils)
library(stats)
library(MASS)
library(wordcloud)
library(syuzhet)
library(qdap)

# tagger_path <- "/home/jm/Documents/stanford-corenlp-full-2015-12-09"
# stanford_vector <- get_sentiment(get_sentences(data_n$STATUS), method = "stanford", tagger_path)

fw <- function.words

data_n <- readr::read_csv("~/Documents/python-notebook/raw_data/data_utf8.csv")
data_n$StringLength <- stri_length(data_n$STATUS)

for (i in 1:length(data_n$STATUS)) {
  data_n$Number_of_Words[[i]] <- stri_count_words(data_n$STATUS[i])
  data_n$Number_of_Dots[[i]] <- stri_count_fixed(data_n$STATUS[i], ".")
  data_n$Number_of_Commas[[i]] <- stri_count_fixed(data_n$STATUS[i], ",")
  data_n$Number_of_Semicolons[[i]] <- stri_count_fixed(data_n$STATUS[i], ";")
  data_n$Number_of_Colons[[i]] <- stri_count_fixed(data_n$STATUS[i], ":")
  data_n$Avarage_Word_Lenght[[i]] <- round((data.frame(t(stri_stats_latex(data_n$STATUS[i])))$CharsWord / data_n$Number_of_Words[[i]]), 3)
  data_n$POS_sentiment[[i]] <- get_nrc_sentiment(data_n$STATUS[i])$positive
  data_n$NEG_sentiment[[i]] <- get_nrc_sentiment(data_n$STATUS[i])$negative
  data_n$OverAll_sentiment[[i]] <- (data_n$NEG_sentiment[[i]]*-1) + data_n$POS_sentiment[[i]]
}

for (k in 1:length(data_n$STATUS)) {
  splittedWords <- gsub("[^[:alnum:][:space:]']", "", tolower(stri_split_fixed(data_n$STATUS[k], " ")[[1]]))
  dfmStatus <- dfm(data_n$STATUS[k], verbose = F, removeNumbers = F, removePunct = F, removeSeparators = F)
  
  data_n$Lexical_Diversity[[k]] <- round(quanteda::lexdiv(dfmStatus, measure = "TTR"), 3)
  data_n$Number_of_FunctionalWords[[k]] <- sum(splittedWords %in% fw)
}


data_n$Avarage_Word_Lenght[is.nan(data_n$Avarage_Word_Lenght)] <- 0
colnames(data_n)[1] <- "#AUTHID"
write.csv(data_n, "~/Documents/python-notebook/raw_data/data_n.csv")





