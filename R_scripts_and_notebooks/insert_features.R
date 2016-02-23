# https://github.com/Rexamine/stringi/issues/212
# https://stat.ethz.ch/pipermail/r-help/2006-May/105280.html
# https://stackoverflow.com/questions/8697079/remove-all-punctuation-except-apostrophes-in-r
# https://github.com/Charudatt89/Personality_Recognition/blob/master/22-9-PersonalityRecognition/SourceCode/FEATURE_BASED_APPROACH/source_code/pos_tagging_2.py
# https://en.wikipedia.org/wiki/English_personal_pronouns

# library(openNLP)
# library(NLP)
# library(RWeka)
# library(RWekajars)
library(stringi)
library(stringr)
library(quanteda)
library(SnowballC)
library(readr)
# library(wordcloud)
library(syuzhet)
library(qdap)
# library(lubridate)
library(jsonlite)

# tagger_path <- "/home/jm/Documents/stanford-corenlp-full-2015-12-09"
# stanford_vector <- get_sentiment(get_sentences(data_n$STATUS), method = "stanford", tagger_path)

fw <- function.words

# Personal pronouns
first_person_singular <- c('I', 'i','me','my','mine', 'myself')
second_person_sing_plu = c('you', 'your','yours', 'yourself', 'yourselves')
third_person_singular = c( 'he','she','it','his','her','hers','its','him', 'himself', 'herself', 'itself')
first_person_plural = c( 'we','us','our','ours', "ourselves")
third_person_plural = c( 'they','them','their','theirs','themselves')

personalPronouns <- c(first_person_singular, second_person_sing_plu, third_person_singular, first_person_plural, third_person_plural)

# Parsing data if needed
# parse_date_time("06/19/09 03:21 PM", "mdy IM p")

data_sentiment <- fromJSON("~/Documents/caseSolvingSeminar/raw_data/setiment_data_scripts/community-sentiment-mashape-com/result2.json")
data_sentiment$confidence <- data_sentiment$result$confidence
data_sentiment$Sentiment_Word <- data_sentiment$result$sentiment
data_sentiment$Sentiment_Numeric <- ifelse(data_sentiment$Sentiment_Word == "Neutral", 2, 
                                           ifelse(data_sentiment$Sentiment_Word == "Positive", 1, 0)
)
data_sentiment$result <- NULL

data_n <- readr::read_csv("~/Documents/caseSolvingSeminar/raw_data/data_utf8.csv")
data_n$StringLength <- stri_length(data_n$STATUS)

for (i in 1:length(data_n$STATUS)) {
  data_n$Number_of_Words[[i]] <- stri_count_words(data_n$STATUS[i])
  data_n$Number_of_Dots[[i]] <- stri_count_fixed(data_n$STATUS[i], ".")
  data_n$Number_of_Commas[[i]] <- stri_count_fixed(data_n$STATUS[i], ",")
  data_n$Number_of_Semicolons[[i]] <- stri_count_fixed(data_n$STATUS[i], ";")
  data_n$Number_of_Colons[[i]] <- stri_count_fixed(data_n$STATUS[i], ":")
  data_n$Average_Word_Length[[i]] <- round((data.frame(t(stri_stats_latex(data_n$STATUS[i])))$CharsWord / data_n$Number_of_Words[[i]]), 3)
  # data_n$POS_sentiment[[i]] <- get_nrc_sentiment(data_n$STATUS[i])$positive
  # data_n$NEG_sentiment[[i]] <- get_nrc_sentiment(data_n$STATUS[i])$negative
  # data_n$OverAll_sentiment[[i]] <- (data_n$NEG_sentiment[[i]]*-1) + data_n$POS_sentiment[[i]]
}

for (k in 1:length(data_n$STATUS)) {
  splittedWords <- gsub("[^[:alnum:][:space:]']", "", tolower(stri_split_fixed(data_n$STATUS[k], " ")[[1]]))
  dfmStatus <- dfm(data_n$STATUS[k], verbose = F, removeNumbers = F, removePunct = F, stem = F, removeSeparators = F)
  
  data_n$Lexical_Diversity[[k]] <- round(quanteda::lexdiv(dfmStatus, measure = "TTR"), 3)
  data_n$Number_of_FunctionalWords[[k]] <- sum(splittedWords %in% fw)
  data_n$Number_of_Pronouns[[k]] <- sum(splittedWords %in% personalPronouns)
  data_n$Number_of_PROPNAMEs[[k]] <- sum(stri_count_fixed(data_n$STATUS[k], "*PROPNAME*"))
}

data_n$SentimentNumeric <- data_sentiment$Sentiment_Numeric
data_n$Average_Word_Length[is.nan(data_n$Average_Word_Length)] <- 0
colnames(data_n)[1] <- "#AUTHID"
write.csv(data_n, "~/Documents/caseSolvingSeminar/raw_data/data_n.csv")

# write.csv(data_n$STATUS, "~/Documents/caseSolvingSeminar/raw_data/data_statuses_only.csv", row.names = FALSE)
# data_n <- readr::read_csv("~/Documents/caseSolvingSeminar/raw_data/data_n.csv")

############# Joined strings
# data_n <- readr::read_csv("~/Documents/caseSolvingSeminar/raw_data/data_n.csv")
# 
# 
# joined_str <- data_n %>%
#   group_by("#AUTHID") %>%
#   paste(data_n$STATUS, collapse=" ")
# 
# myby <- by(data_n$STATUS,data_n$`#AUTHID`,function(x)paste(x,collapse=" "))
# myby <- data.frame(id=c(myby))


