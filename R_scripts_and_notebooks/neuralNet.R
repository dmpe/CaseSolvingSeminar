library(clusterGeneration)
library(nnet)
library(neuralnet)
library(caret)
library(stringi)
library(quanteda)
library(readr)
library(mi)

dataall <- readr::read_csv("~/Documents/python-notebook/raw_data/data_n.csv")
dataall$cEXT <- ifelse(dataall$cEXT == "y", 1, 0)
dataall$cNEU <- ifelse(dataall$cNEU == "y", 1, 0)
dataall$cAGR <- ifelse(dataall$cAGR == "y", 1, 0)
dataall$cCON <- ifelse(dataall$cCON == "y", 1, 0)
dataall$cOPN <- ifelse(dataall$cOPN == "y", 1, 0)

dataWeNeed <- dataall[,c(3:13, 22:29)]

trainIndex <- createDataPartition(dataWeNeed$cCON, p=0.66, list = F)
dataWeNeed.train <- dataWeNeed[trainIndex, ]
dataWeNeed.test <- dataWeNeed[-trainIndex, ]

## Normalisation
mdf <- missing_data.frame(data.frame(dataWeNeed))
show(mdf)

# Model
mod4 <- train(cEXT + cNEU + cAGR + cCON + cOPN ~ ., method='nnet', data=dat.in, linout=T)







