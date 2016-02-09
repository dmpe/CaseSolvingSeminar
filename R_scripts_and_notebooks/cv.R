library(caret)
library(readr)
library("e1071")
library(kernlab)
library(jsonlite)
library(plyr)

dataall <- readr::read_csv("~/Documents/python-notebook/raw_data/data_n.csv")
dataall$cEXT <- as.factor(ifelse(dataall$cEXT == "y", 1, 0))
dataall$cNEU <- as.factor(ifelse(dataall$cNEU == "y", 1, 0))
dataall$cAGR <- as.factor(ifelse(dataall$cAGR == "y", 1, 0))
dataall$cCON <- as.factor(ifelse(dataall$cCON == "y", 1, 0))
dataall$cOPN <- as.factor(ifelse(dataall$cOPN == "y", 1, 0))
dataall <- dataall[,c(3:13, 22:29)]

fitControl <- trainControl(method = "repeatedcv", number = 10)

trainIndex <- createDataPartition(dataall$cCON, p = 0.66, list = F)
dataWeNeed.train <- dataall[trainIndex, ]
dataWeNeed.test <- dataall[-trainIndex, ]

gbmFit1 <- train(cCON ~ ., data = dataWeNeed.train, method = "svmLinear", trControl = fitControl)

#############################

data1_4991 <- fromJSON("~/Documents/python-notebook/raw_data/setiment_data_scripts/text-processing-com/result_1_4991.json")
data4991_end <- fromJSON("~/Documents/python-notebook/raw_data/setiment_data_scripts/text-processing-com/result_4991_end.json")
data_text_sentiment <- rbind.fill(data1_4991,data4991_end)


summary(as.factor(dataall$cEXT))
summary(as.factor(dataall$cNEU))
summary(as.factor(dataall$cAGR))
summary(as.factor(dataall$cCON))
summary(as.factor(dataall$cOPN))


