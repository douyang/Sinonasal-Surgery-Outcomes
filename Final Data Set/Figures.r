setwd("C:\\Users\\David Ouyang\\Dropbox\\StatisticalAnalysis\\Sinonasal\\Final Data Set")
library(ggplot2)


data <- read.csv("ComplicationsOverTime.csv", stringsAsFactors = FALSE)
str(data)
data$count <- 1

PropData <- ddply(data, c("year", "compType"), summarise, count = sum(count))

qplot(data = PropData, year, count, fill = compType, geom = "bar", stat = "identity", position = "stack")

qplot(data = PropData[PropData$compType != "",], year, count, 
fill = compType, geom = "bar", stat = "identity", position = "stack")
+ scale_fill_manual(values = c("red", "grey20", "blue", 
"black", "darkgreen", "lightblue", "grey80"))

qplot(data = PropData[PropData$compType != "",], year, count, 
fill = compType, geom = "bar", stat = "identity", position = "stack") + 
theme_bw() 
ggsave("ComplicationsOverTime.png", width = 6.4, height = 5.2) 

qplot(data = PropData[PropData$compType != "",], year, count, 
fill = compType, geom = "bar", stat = "identity", position = "fill") + theme_bw() 
ggsave("ComplicationsPropOverTime.png", width = 6.4, height = 5.2)

//infectious
qplot(data = PropData[PropData$compType == "infectious",], year, count,
 geom = c("point", "line") ) + geom_smooth( method = "lm")
ggsave("infectious.png")

//electrolyte
qplot(data = PropData[PropData$compType == "Electrolyte",], year, count,
 geom = c("point", "line") ) + geom_smooth( method = "lm")
ggsave("electrolyte.png")

//Cardiopulm
qplot(data = PropData[PropData$compType == "Cardiopulm",], year, count,
 geom = c("point", "line") ) + geom_smooth( method = "lm")
ggsave("Cardiopulm.png")

qplot(data = PropData[PropData$compType == "death",], year, count,
 geom = c("point", "line") ) +ylim(0, 8) + geom_smooth(method = "lm")

ggsave("DeathOverTime.png", , width = 6.4, height = 5.2)

qplot(data = PropData[PropData$compType == "death",], year, count,
 geom = "bar", stat = "identity")  + geom_smooth(method = "lm")


ggsave("DeathOverTime2.png", , width = 6.4, height = 5.2)

# + scale_fill_manual(values = c("darkred", "grey20", muted("blue"), "grey", muted("lightgreen"), "blue", "grey80"))


data <- read.csv("subsetNeckDissection.csv", stringsAsFactors = FALSE)
str(data)
numNeck <- ddply(data, c("year"), summarise, comp = sum(comp), count = sum(count))
sum(numNeck$count)
numNeck$type <- "neck"

data <- read.csv("subsetNeurosurgery.csv", stringsAsFactors = FALSE)
str(data)
numNeuro <- ddply(data, c("year"), summarise, comp = sum(comp), count = sum(count))
sum(numNeuro$count)
numNeuro$type <- "neuro"

data <- read.csv("subsetOrbitMax.csv", stringsAsFactors = FALSE)
str(data)
numOrbit <- ddply(data, c("year"), summarise, comp = sum(comp), count = sum(count))
sum(numOrbit$count)
numOrbit$type <- "orbit"

combined <- rbind(numOrbit, numNeuro, numNeck)

qplot(data = combined, year, count, fill = type, 
geom = "bar", stat = "identity", position = "dodge") + geom_smooth( method = "lm") + facet_grid(~type)
ggsave("ComplicatedCasesOverTime.png", width = 12.8, height = 5.2)

qplot(data = combined, year, count, fill = type, 
geom = "bar", stat = "identity", position = "stack") + theme_bw()
ggsave("ComplicatedCasesOverTime.png", width = 6.4, height = 5.2)

data <- read.csv("surgicalCasesWComplications.csv", stringsAsFactors = TRUE)
data$count <- 1 





qplot(data = data[data$pay1 > 0,], factor(year), fill = factor(pay1), geom = "bar", 
binwidth = 1, position = "fill") +   scale_fill_grey() + theme_bw()  + 
scale_y_continuous("Proportion") + scale_x_discrete("Year")  + opts(axis.text.x=theme_text(angle=-90))
ggsave("Payer Over Time.png")

qplot(data = data[data$race > 0,], factor(year), fill = factor(race), geom = "bar", 
binwidth = 1, position = "fill") +   scale_fill_grey() + theme_bw() +
scale_y_continuous("Proportion") + scale_x_discrete("Year")  + opts(axis.text.x=theme_text(angle=-90))
ggsave("Race Over Time.png")


qplot(data = data, factor(year), age, geom = "boxplot") + ylim(0, 100) + theme_bw() + 
opts(axis.text.x=theme_text(angle=-90)) 
ggsave("Age Over Time.png")

