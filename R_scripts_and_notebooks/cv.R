library(caret)
library(readr)
library("e1071")
library(kernlab)

dataall <- readr::read_csv("~/Documents/python-notebook/raw_data/data_n.csv")
# dataall$cEXT <- as.factor(ifelse(dataall$cEXT == "y", 1, 0))
# dataall$cNEU <- as.factor(ifelse(dataall$cNEU == "y", 1, 0))
# dataall$cAGR <- as.factor(ifelse(dataall$cAGR == "y", 1, 0))
# dataall$cCON <- as.factor(ifelse(dataall$cCON == "y", 1, 0))
# dataall$cOPN <- as.factor(ifelse(dataall$cOPN == "y", 1, 0))

dataall$cEXT <- ifelse(dataall$cEXT == "y", 1, 0)
dataall$cNEU <- ifelse(dataall$cNEU == "y", 1, 0)
dataall$cAGR <- ifelse(dataall$cAGR == "y", 1, 0)
dataall$cCON <- ifelse(dataall$cCON == "y", 1, 0)
dataall$cOPN <- ifelse(dataall$cOPN == "y", 1, 0)
dataall <- dataall[,c(3:13, 22:29)]



# Model 0
fitControl <- trainControl(## 10-fold CV
  method = "repeatedcv",
  number = 10)

trainIndex <- createDataPartition(dataall$cCON, p=0.66, list = F)
dataWeNeed.train <- dataall[trainIndex, ]
dataWeNeed.test <- dataall[-trainIndex, ]


gbmFit1 <- train(cCON ~ ., data = dataWeNeed.train, method = "svmLinear",
                 trControl = fitControl)



