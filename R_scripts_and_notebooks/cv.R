library(caret)
library(readr)
library(e1071)
library(kernlab)
library(jsonlite)
library(plyr)

set.seed(5152)

dataall <- readr::read_csv("~/Documents/caseSolvingSeminar/raw_data/data_n.csv")
dataall$cEXT <- as.factor(ifelse(dataall$cEXT == "y", 1, 0))
dataall$cNEU <- as.factor(ifelse(dataall$cNEU == "y", 1, 0))
dataall$cAGR <- as.factor(ifelse(dataall$cAGR == "y", 1, 0))
dataall$cCON <- as.factor(ifelse(dataall$cCON == "y", 1, 0))
dataall$cOPN <- as.factor(ifelse(dataall$cOPN == "y", 1, 0))
dataall <- dataall[,12:33]
dataall <- dataall[,c(1, 11:22)]

fitControl <- trainControl(method = "repeatedcv", number = 10, repeats = 2, seeds = 5152)

trainIndex <- createDataPartition(dataall$cCON, p = 0.66, list = F)
dataWeNeed.train <- dataall[trainIndex, ]
dataWeNeed.test <- dataall[-trainIndex, ]


gbmFit1 <- train(cCON ~ ., data = dataWeNeed.train, method = "svmLinear", trControl = fitControl)
gbmFit1

knnPredict1 <- predict(gbmFit1, newdata = dataWeNeed.test)
cmat1 <- confusionMatrix(data = knnPredict1, reference = dataWeNeed.test$cCON)
cmat1

#############################


dataYPREDextBNB <- readr::read_csv("raw_data/y_pred_class_labels/ext_predtt BernoulliNB.csv", col_names = F)
dataEXTtest <- readr::read_csv("raw_data/test_class_labels/ext_test.csv", col_names = F)


cmat1 <- confusionMatrix(data = dataYPREDextBNB$X1, reference = dataEXTtest$X2, positive = "1")
cmat1


#############################

data1_4991 <- fromJSON("~/Documents/caseSolvingSeminar/raw_data/setiment_data_scripts/text-processing-com/result_1_4991.json")
data4991_end <- fromJSON("~/Documents/caseSolvingSeminar/raw_data/setiment_data_scripts/text-processing-com/result_4991_end.json")
data_text_sentiment <- rbind.fill(data1_4991, data4991_end)


summary(as.factor(dataall$cEXT))
summary(as.factor(dataall$cNEU))
summary(as.factor(dataall$cAGR))
summary(as.factor(dataall$cCON))
summary(as.factor(dataall$cOPN))


