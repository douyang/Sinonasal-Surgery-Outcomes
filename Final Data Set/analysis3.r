setwd("C:\\Users\\David Ouyang\\Dropbox\\StatisticalAnalysis\\Sinonasal\\Final Data Set")
library(ggplot2)


data <- read.csv("surgicalCasesWComplicationsIsDifficult3.csv", stringsAsFactors = FALSE)
str(data)


sum(data$complications)
sum(data$died)
937/3850
30/3850

subset <- data[data$hospital %in% c(25061, 36194, 48006, 26099, 6081, 36234, 42323, 13072, 39161, 
36125, 6626, 24085, 27108, 53109, 36257, 12007, 37006, 29185, 12203, 19136, 6407, 20060, 4117, 41051, 48263, 
17109, 47030, 12265, 6525, 17207, 36147, 39033),]
notsubset <- data[!data$hospital %in% c(25061, 36194, 48006, 26099, 6081, 36234, 42323, 13072, 39161, 
36125, 6626, 24085, 27108, 53109, 36257, 12007, 37006, 29185, 12203, 19136, 6407, 20060, 4117, 41051, 48263, 
17109, 47030, 12265, 6525, 17207, 36147, 39033),]



t.test(subset[subset$isDifficult == 1 & subset$los>-1,]$los,notsubset[notsubset$isDifficult == 1 &notsubset$los>-1,]$los)
t.test(subset[subset$isDifficult == 0 & subset$los>-1,]$los,notsubset[notsubset$isDifficult == 0 &notsubset$los>-1,]$los)
t.test(subset[subset$los>-1,]$los,notsubset[notsubset$los>-1,]$los)

summary(notsubset[notsubset$isDifficult == 0 &notsubset$los>-1,]$los)
str(notsubset[notsubset$isDifficult == 0 &notsubset$los>-1,]$los)
summary(data[data$isDifficult == 0 &data$los>-1,]$los)
str(data[data$isDifficult == 0 &data$los>-1,]$los)

294/3850
sum(subset$complications)
69/294

sum(data$complications)
937/3850


sum(subset[subset$isDifficult == 1,]$complications)
str(subset[subset$isDifficult == 1,])
28/84


sum(data[data$isDifficult == 1,]$complications)
str(data[data$isDifficult == 1,])
210/715

mean(subset[subset$los>-1,]$los)
mean(subset[subset$isDifficult == 1 & subset$los>-1,]$los)

mean(data[data$los>-1,]$los)
mean(data[data$isDifficult == 1 & data$los>-1,]$los)


mean(data[data$isDifficult == 1 & data$los>-1,]$los)
mean(data[data$isDifficult == 0 & data$los>-1,]$los)

sum(data[data$isDifficult == 0,]$complications)
str(data[data$isDifficult == 0,])
727/3135

data <- read.csv("subsetNeckDissection.csv", stringsAsFactors = FALSE)
subset <- data[data$hospital %in% c(25061, 36194, 48006, 26099, 6081, 36234, 42323, 13072, 39161),]
str(data)
str(subset)

29/244

data <- read.csv("subsetNeurosurgery.csv", stringsAsFactors = FALSE)
subset <- data[data$hospital %in% c(25061, 36194, 48006, 26099, 6081, 36234, 42323, 13072, 39161),]
str(data)
str(subset)

27/297

data <- read.csv("subsetOrbitMax.csv", stringsAsFactors = FALSE)
subset <- data[data$hospital %in% c(25061, 36194, 48006, 26099, 6081, 36234, 42323, 13072, 39161),]
str(data)
str(subset)

42/236