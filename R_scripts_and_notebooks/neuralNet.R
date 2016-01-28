library(clusterGeneration)
library(nnet)
library(neuralnet)
library(caret)
library(readr)
#library(mi)
#library(betareg)
library(scales)
library(h2o)
library(mxnet)

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

## Normalisation
#mdf <- missing_data.frame(data.frame(dataWeNeed.test))
#show(mdf)

maxs <- apply(dataall[,2:6], 2, max)
mins <- apply(dataall[,2:6], 2, min)
dataall[,2:6] <- as.data.frame(scale(dataall[,2:6], center = mins, scale = maxs - mins))

maxs <- apply(dataall[,12:18], 2, max)
mins <- apply(dataall[,12:18], 2, min)
dataall[,12:18] <- as.data.frame(scale(dataall[,12:18], center = mins, scale = maxs - mins))


# Split
trainIndex <- createDataPartition(dataall$cCON, p=0.66, list = F)
dataWeNeed.train <- dataall[trainIndex, ]
dataWeNeed.test <- dataall[-trainIndex, ]

### Model #1 - nnet
mod4 <- train(cEXT + cNEU + cAGR + cCON + cOPN ~ ., method='nnet', data=dataWeNeed.train,  size = 5)
prestige.predict <- predict(mod4, newdata = dataWeNeed.test)
prestige.rmse <- sqrt(mean((prestige.predict - prestige.test$income)^2))

### Model #2 - neuralnet; requires integers not factors in binary variables
# https://stackoverflow.com/questions/17457028/working-with-neuralnet-in-r-for-the-first-time-get-requires-numeric-complex-ma
# https://stackoverflow.com/questions/17794575/error-in-terms-formulaformula-in-formula-and-no-data-argument
# http://gekkoquant.com/2012/05/26/neural-networks-with-r-simple-example/
# http://www.r-bloggers.com/fitting-a-neural-network-in-r-neuralnet-package/

n <- names(dataWeNeed.train)
f <- as.formula(paste("cEXT + cNEU + cAGR + cCON + cOPN ~", paste(n[!n %in% c("STATUS", "cEXT","cNEU", "cAGR", "cCON", "cOPN")], collapse = " + ")))
mdl <- neuralnet(f, data=dataWeNeed.train, hidden=5, threshold=0.01)
print(mdl)

net.results <- compute(mdl, dataWeNeed.test)
ls(net.results)
print(net.results$net.result)

#Lets display a better version of the results
cleanoutput <- cbind(dataWeNeed.test,sqrt(dataWeNeed.test),
                     as.data.frame(net.results$net.result))

colnames(cleanoutput) <- c("Input","Expected Output","Neural Net Output")
print(cleanoutput)





### Model #3 - h2o, can only work with one 'y'
localH2O = h2o.init(nthreads = -1)
dataWeNeed.train_h2o <- as.h2o(dataWeNeed.train, destination_frame = 'dataWeNeed.train_h2o')
dataWeNeed.test_h2o <- as.h2o(dataWeNeed.test, destination_frame = 'dataWeNeed.test_h2o')
model <- h2o.deeplearning( x = 12:19,  # column numbers for predictors
                           y = 7,   # column number for label
                           training_frame = dataWeNeed.train_h2o, # data in H2O format
                           activation = "TanhWithDropout", # or 'Tanh'
                           input_dropout_ratio = 0.2, # % of inputs dropout
                           hidden_dropout_ratios = c(0.5,0.5,0.5), # % for nodes dropout
                           hidden = c(50,50,50), # three layers of 50 nodes
                           epochs = 100) # max. no. of epochs

h2o_yhat_test <- h2o.predict(model, dataWeNeed.test_h2o)
df_yhat_test <- as.data.frame(h2o_yhat_test)

## Model 4

dmt <- data.matrix(dataWeNeed.train[2:19])
dmtt <- data.matrix(dataWeNeed.test[2:19])

mx.set.seed(5152)
model <- mx.mlp(dmt[,10:18],dmt[,8], hidden_node=8, out_node=2, out_activation="softmax",
                num.round=20, array.batch.size=15, learning.rate=0.07, momentum=0.9,
                eval.metric=mx.metric.accuracy)

preds = predict(model, dmtt[,10:18])
pred.label = max.col(t(preds))-1
table(pred.label, dmtt[,8])

