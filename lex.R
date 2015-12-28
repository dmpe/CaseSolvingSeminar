library(openNLP)
library(NLP)
library(rJava)
library(RWeka)
library(stringi)
library(readr)

data_n <-  readr::read_csv("~/Documents/python-notebook/data_utf8.csv")
data_n$StringLength <- stri_length(data_n$STATUS)
