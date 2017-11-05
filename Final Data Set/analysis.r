setwd("C:\\Users\\David Ouyang\\Dropbox\\StatisticalAnalysis\\Sinonasal\\Final Data Set")
library(ggplot2)


data <- read.csv("surgicalCasesWComplications.csv", stringsAsFactors = FALSE)
str(data)
sum(data$comp)

sum(data[data$volume == "high",]$died)
4/1097
sum(data[data$volume == "medium",]$died)
11/1939
sum(data[data$volume == "low",]$died)
15/814


sum(data[data$volume == "high",]$comp) - 4
183/1097
sum(data[data$volume == "medium",]$comp) - 11
287/1939
sum(data[data$volume == "low",]$comp) - 15
102/814


modelCompl <- lm(data$comp ~ relevel(factor(data$volume), "high") + data$age + data$pay1 + data$year + factor(data$d1))
modelCompl <- lm(data$comp ~ relevel(factor(data$volume), "high") + data$age + data$pay1 + data$year +  factor(data$p1))
summary(modelCompl)


str(data)
qplot(data$age, binwidth = 1) + xlim(0, 100)
qplot(data$year)

qplot(data[data$complication == 0,]$charges, fill = data[data$complication == 0,]$complication, binwidth = 1000) + xlim(0, 400000)

qplot(data[data$complication == 1,]$charges, fill = data[data$complication == 1,]$complication, binwidth = 1000) + xlim(0, 400000)


qplot(data[data$complication == 0,]$los, binwidth = 1) + xlim(0, 50)
qplot(data[data$complication == 1,]$los, binwidth = 1) + xlim(0, 50)
mean(data[data$complication == 0 & data$los > 0,]$los)
mean(data[data$complication == 1& data$los > 0,]$los)


complicationRates <- ddply(data, c("p1"), summarise, propComplication = sum(comp)/sum(count), num = sum(count))

write.csv( arrange(complicationRates, desc(propComplication)), "ComplicationProportionByProcedure.csv")


data <- read.csv("surgicalCasesWComplications.csv")
summary(data)


data <- read.csv("subsetNeckDissection.csv")
summary(data)

data <- read.csv("subsetOrbitMax.csv")
summary(data)

data <- read.csv("subsetNeurosurgery.csv")
summary(data)



