setwd("C:\\Users\\David Ouyang\\Dropbox\\StatisticalAnalysis\\Sinonasal\\Final Data Set")
library(ggplot2)


data <- read.csv("surgicalCasesWComplications.csv", stringsAsFactors = FALSE)
str(data)

qplot(data$year, binwidth = 1, fill = data$volume)
ggsave("trendOverTime.png")

data[data$volume != "high",]$volume <- "low"
qplot(data$year, binwidth = 1, fill = data$volume, position = "fill") + scale_fill_manual(values = c("black", "grey80", "grey80"))
 




mean(data[data$age > 0,]$age)

3850 - 1097

879 - 32

244 - 79

236 - 106

558 - 255


str( data[data$hospitalClass == "high",])
mean(data[data$hospitalClass == "high" & data$age > 0,]$age)
sd(data[data$hospitalClass == "high" & data$age > 0,]$age)

table(data[data$hospitalClass == "high",]$sex)
table(data[data$hospitalClass == "high",]$sex)/1061

mean(data[data$hospitalClass == "high" & data$los > 0,]$los)
sd(data[data$hospitalClass == "high" & data$los > 0,]$los)

table(data[data$hospitalClass == "high",]$race)

table(data[data$hospitalClass == "high",]$pay1)

table(data[data$hospitalClass == "high",]$race)/1061

table(data[data$hospitalClass == "high",]$pay1)/1061





str( data[data$hospitalClass != "high",])
mean(data[data$hospitalClass != "high" & data$age > 0,]$age)
sd(data[data$hospitalClass != "high" & data$age > 0,]$age)

table(data[data$hospitalClass != "high",]$sex)
table(data[data$hospitalClass != "high",]$sex) / 2789 

mean(data[data$hospitalClass != "high" & data$los > 0,]$los)
sd(data[data$hospitalClass != "high" & data$los > 0,]$los)

table(data[data$hospitalClass != "high",]$race)

table(data[data$hospitalClass != "high",]$pay1)

table(data[data$hospitalClass != "high",]$race)/  2789 

table(data[data$hospitalClass != "high",]$pay1)/  2789 


numPerYear <- ddply(data, c("year", "volume"), summarise, count = sum(count))
qplot(data = numPerYear, year, count, color = volume, geom = "line")


numPerYearTotal <- ddply(data, c("year"), summarise, count = sum(count))
qplot(data = numPerYearTotal , year, count, geom = c("point")) + geom_smooth(method = "lm")
qplot(data = numPerYearTotal , year, count, geom = c("bar"), stat = "identity") + geom_smooth(method = "lm") + ylim(0, 250)
ggsave("OverAllTrend.png", width = 6.4, height = 5.2)

Proportion <-  merge(numPerYearTotal, numPerYear[numPerYear$volume == "high",], by = "year")
Proportion$prop <- Proportion$count.y / Proportion$count.x
qplot(Proportion$year, Proportion$prop, geom = "line")
qplot(Proportion$year, Proportion$prop, geom = "line") + geom_smooth(method = "lm")
qplot(Proportion$year, Proportion$prop, geom = "bar", stat = "identity") + geom_smooth(method = "lm") + ylim(0, .6)
ggsave("PropOverTime.png", width = 6.4, height = 5.2)

model <- lm(Proportion$prop ~ Proportion$year)
summary(model)

model <- lm(Proportion$count.y ~ Proportion$year)
summary(model)


#Urban
x <- as.table(rbind(c(27, 3), c(346, 482)))
chisq.test(x)

#Teaching
x <- as.table(rbind(c(29, 1), c(707, 121)))
chisq.test(x)

#Large
x <- as.table(rbind(c(22, 8), c(461, 367)))
chisq.test(x)




#Complication Rates between Hospitals Volume, Complications, Type of Surg

data <- read.csv("surgicalCasesWComplications.csv", stringsAsFactors = FALSE)
data$high <- data$volume == "high"
ddply(data, c("high", "complications"), summarise, count = sum(count))

chisq.test(as.table(rbind(c(2338,415), c(910,  187))))



data <- read.csv("subsetNeckDissection.csv", stringsAsFactors = FALSE)
str(data)
data$high <- data$volume == "high"
ddply(data, c("high", "complications"), summarise, count = sum(count))
chisq.test(as.table(rbind(c(138,27), c(64,  15))))

data <- read.csv("subsetNeurosurgery.csv", stringsAsFactors = FALSE)
str(data)
data$high <- data$volume == "high"
ddply(data, c("high", "complications"), summarise, count = sum(count))
chisq.test(as.table(rbind(c(131,38), c(97,  31))))

data <- read.csv("subsetOrbitMax.csv", stringsAsFactors = FALSE)
str(data)
data$high <- data$volume == "high"
ddply(data, c("high", "complications"), summarise, count = sum(count))
chisq.test(as.table(rbind(c(100,30), c(75,  31))))


#Deaths
chisq.test(as.table(rbind(c(1057,4), c(2763,  26))))

#Deaths
chisq.test(as.table(rbind(c(1061 - 424,424), c(2789 - 998,  998 ))))

#Infectious
chisq.test(as.table(rbind(c(1061 - 42,42), c(2789 - 146,  146))))

#Cardiopulmonary
chisq.test(as.table(rbind(c(1061 - 223,223), c(2789 - 496,  496))))


chisq.test(as.table(rbind(c(1061 - 13,13), c(2789 - 38,  38))))
chisq.test(as.table(rbind(c(1061 - 20,20), c(2789 - 56,  56))))
chisq.test(as.table(rbind(c(1061 - 12,12), c(2789 - 34,  34))))
chisq.test(as.table(rbind(c(1061 - 110,110), c(2789 - 202,  202))))


data <- read.csv("surgicalCasesWComplicationsIsDifficult3.csv", stringsAsFactors = FALSE)
str(data)
data$high <- data$volume == "high"
ddply(data, c("high", "isDifficult"), summarise, count = sum(complications))

chisq.test(as.table(rbind(c(1061 - 89,89), c(2789 - 121,  121))))

 str(data[data$isDifficult == TRUE & data$high == TRUE,])
//277 complicated/high

 str(data[data$isDifficult == TRUE & data$high != TRUE,])
//438 complicated/not high

89/277
121/438

 str(data[data$isDifficult == TRUE & data$died ==1 & data$high == TRUE,])
//2 died

 str(data[data$isDifficult == TRUE & data$died ==1 & data$high != TRUE,])
//6 died

chisq.test(as.table(rbind(c(277 - 2,2), c(438 - 6,  6))))

mean(data[data$isDifficult == TRUE & data$los > 0,]$los)
sd((data[data$isDifficult == TRUE & data$los > 0,]$los))
//9.369, 715 cases, 9.208

mean(data[data$isDifficult != TRUE & data$los > 0,]$los)
sd((data[data$isDifficult != TRUE & data$los > 0,]$los))
//6.18399, 3098 cases, 7.6449

t.test(data[data$isDifficult == TRUE & data$los > 0,]$los, data[data$isDifficult != TRUE & data$los > 0,]$los)


t.test(data[data$isDifficult == TRUE,]$complications, data[data$isDifficult != TRUE,]$complications)



//Gender Changes Over Time
qplot(data = data[data$sex > -.1,], year, count, stat = "identity", geom = "bar", fill = sex) + facet_wrap(~sex) + geom_smooth(method = "lm")


data <- read.csv("surgicalCasesWComplicationsIsDifficult3.csv", stringsAsFactors = FALSE)
data$count<-1
ddply(data, c("isDifficult", "complications"), summarise, count = sum(count))
chisq.test(as.table(rbind(c(2408,727), c(505,  210))))
727/(2408+727)
210/(210+505)


