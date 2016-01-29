# https://github.com/Rexamine/stringi/issues/212

library(openNLP)
library(NLP)
library(RWeka)
library(RWekajars)
library(stringi)
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

data_n <- readr::read_csv("~/Documents/python-notebook/raw_data/data_utf8.csv")
data_n$StringLength <- stri_length(data_n$STATUS)

for (i in 1:length(data_n$STATUS)) {
  data_n$Number_of_Words[[i]] <- stri_count_words(data_n$STATUS[i])
  data_n$Number_of_Dots[[i]] <- stri_count_fixed(data_n$STATUS[i], ".")
  data_n$Number_of_Commas[[i]] <- stri_count_fixed(data_n$STATUS[i], ",")
  data_n$Number_of_Semicolons[[i]] <- stri_count_fixed(data_n$STATUS[i], ";")
  data_n$Number_of_Colons[[i]] <- stri_count_fixed(data_n$STATUS[i], ":")
  data_n$Avarage_Word_Lenght[[i]] <- round((data.frame(t(stri_stats_latex(data_n$STATUS[i])))$CharsWord / data_n$Number_of_Words[[i]]), 3)
}

for (k in 1:length(data_n$STATUS)) {
  dfmStatus <- dfm(data_n$STATUS[k], verbose = F, removeNumbers = F, removePunct = F, removeSeparators = F)
  sentimentAna <- get_nrc_sentiment(data_n$STATUS[k])
  data_n$Lexical_Diversity[[k]] <- round(quanteda::lexdiv(dfmStatus, measure = "TTR"), 3)
  data_n$POS_sentiment[[k]] <- sentimentAna$positive
  data_n$NEG_sentiment[[k]] <- sentimentAna$negative
}

data_n$Avarage_Word_Lenght[is.nan(data_n$Avarage_Word_Lenght)] <- 0

colnames(data_n)[1] <- "#AUTHID" ## WTF?
write.csv(data_n, "~/Documents/python-notebook/raw_data/data_n.csv")
